#!/usr/bin/env python
"""
section_transports.py

Compute monthly volume-transport time series for a set of user-defined
ocean sections (specified in a YAML file) and write them to a single
netCDF file.

Transport component is chosen automatically from the section geometry:
  lon1 == lon2  →  umo  (mass X-transport, kg/s)  fixed-longitude section
  lat1 == lat2  →  vmo  (mass Y-transport, kg/s)  fixed-latitude  section

The nearest grid column/row is found using the 1-D tracer-grid coordinates
xh (cell-centre longitudes) and yh (cell-centre latitudes).  The same index
is then applied to the staggered coordinate (xq / yq) that carries umo / vmo.

Usage:
  python section_transports.py diag_config.yml section_transports.yml
  python section_transports.py diag_config.yml section_transports.yml -nw 8

Output:
  ncfiles/<casename>_custom_section_transports.nc
"""

import os, sys, glob, yaml, argparse
import numpy as np
import xarray as xr
from datetime import datetime
from mom6_tools.m6toolbox import cime_xmlquery, add_global_attrs

# Reference seawater density for kg/s → m³/s conversion
RHO_0 = 1035.0   # kg m⁻³
# 1 Sverdrup = 10⁶ m³/s
SV    = 1.0e6    # m³/s


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description='Compute monthly transport time series for custom sections.',
        epilog='Written by Gustavo Marques (gmarques@ucar.edu).')
    parser.add_argument('diag_config_yml_path', type=str,
        help='Full path to diag_config.yml describing the CESM/MOM6 run.')
    parser.add_argument('section_transports_yml_path', type=str,
        help='Full path to section_transports.yml defining the sections.')
    parser.add_argument('-sd', '--start_date', type=str, default='',
        help='Start date (YYYY-MM-DD). Defaults to value in diag_config.yml.')
    parser.add_argument('-ed', '--end_date', type=str, default='',
        help='End date (YYYY-MM-DD). Defaults to value in diag_config.yml.')
    parser.add_argument('-nw', '--number_of_workers', type=int, default=0,
        help='Dask workers (0 = serial, default).')
    parser.add_argument('-debug', action='store_true',
        help='Print extra debugging information.')
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Section helpers
# ---------------------------------------------------------------------------

def load_sections(yml_path):
    """Return dict of section definitions from the YAML file."""
    with open(yml_path, 'r') as f:
        cfg = yaml.load(f, Loader=yaml.Loader)
    return cfg['sections']


def infer_component(name, lon1, lon2, lat1, lat2):
    """Return 'umo' for fixed-longitude sections, 'vmo' for fixed-latitude."""
    if lon1 == lon2:
        return 'umo'
    elif lat1 == lat2:
        return 'vmo'
    else:
        raise ValueError(
            f"Section '{name}': endpoints must share either longitude "
            f"(lon1==lon2) or latitude (lat1==lat2). "
            f"Got lon=({lon1},{lon2}), lat=({lat1},{lat2}).")


# ---------------------------------------------------------------------------
# Transport extraction
# ---------------------------------------------------------------------------

def extract_transport(ds, name, lon1, lon2, lat1, lat2, component, debug=False):
    """
    Return a DataArray of transport [Sv] as a function of time.

    Parameters
    ----------
    ds        : xarray.Dataset  – multi-file z dataset (lazy / dask)
    name      : str             – human-readable section name
    lon1,lon2 : float           – section longitude endpoints
    lat1,lat2 : float           – section latitude endpoints
    component : 'umo' | 'vmo'
    debug     : bool
    """
    xh = ds['xh'].values   # 1-D cell-centre longitudes
    yh = ds['yh'].values   # 1-D cell-centre latitudes

    if component == 'umo':
        # -------------------------------------------------------------------
        # Fixed longitude → umo (time, z_l, yh, xq)
        # Find nearest xh index; apply that index to the staggered xq axis.
        # Integrate over depth (z_l) and the latitude band (yh).
        # -------------------------------------------------------------------
        lon = lon1   # lon1 == lon2
        i_xh = int(np.argmin(np.abs(xh - lon)))
        da = ds['umo'].isel(xq=i_xh)        # (time, z_l, yh)

        if debug:
            print(f'  [{name}] umo: nearest xh={xh[i_xh]:.4f} (target={lon}), '
                  f'xq={float(ds.xq[i_xh]):.4f}')

        # latitude slice on the yh coordinate already present in da
        da = da.sel(yh=slice(lat1, lat2))

        if debug:
            print(f'  [{name}] yh range: {float(da.yh.min()):.4f} '
                  f'to {float(da.yh.max()):.4f} ({da.yh.size} points)')

        transport_kgs = da.sum(dim=['z_l', 'yh'])

    else:
        # -------------------------------------------------------------------
        # Fixed latitude → vmo (time, z_l, yq, xh)
        # Find nearest yh index; apply that index to the staggered yq axis.
        # Integrate over depth (z_l) and the longitude band (xh).
        # -------------------------------------------------------------------
        lat = lat1   # lat1 == lat2
        j_yh = int(np.argmin(np.abs(yh - lat)))
        da = ds['vmo'].isel(yq=j_yh)        # (time, z_l, xh)

        if debug:
            print(f'  [{name}] vmo: nearest yh={yh[j_yh]:.4f} (target={lat}), '
                  f'yq={float(ds.yq[j_yh]):.4f}')

        # longitude slice on the xh coordinate already present in da
        da = da.sel(xh=slice(lon1, lon2))

        if debug:
            print(f'  [{name}] xh range: {float(da.xh.min()):.4f} '
                  f'to {float(da.xh.max()):.4f} ({da.xh.size} points)')

        transport_kgs = da.sum(dim=['z_l', 'xh'])

    # kg/s  →  Sv  (= 10⁶ m³/s, using constant reference density)
    transport_sv = transport_kgs / (RHO_0 * SV)
    return transport_sv


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main():
    args = parse_args()

    # ---- directories -------------------------------------------------------
    os.makedirs('ncfiles', exist_ok=True)

    # ---- read diag config --------------------------------------------------
    diag_cfg = yaml.load(open(args.diag_config_yml_path, 'r'), Loader=yaml.Loader)

    caseroot   = diag_cfg['Case']['CASEROOT']
    casename   = cime_xmlquery(caseroot, 'CASE')
    DOUT_S     = cime_xmlquery(caseroot, 'DOUT_S')
    if DOUT_S:
        OUTDIR = cime_xmlquery(caseroot, 'DOUT_S_ROOT') + '/ocn/hist/'
    else:
        OUTDIR = cime_xmlquery(caseroot, 'RUNDIR') + '/'

    avg        = diag_cfg['Avg']
    start_date = args.start_date if args.start_date else avg['start_date']
    end_date   = args.end_date   if args.end_date   else avg['end_date']
    z_pattern  = casename + diag_cfg['Fnames']['z']

    print('─' * 60)
    print(f'Case        : {casename}')
    print(f'OUTDIR      : {OUTDIR}')
    print(f'Date range  : {start_date} → {end_date}')
    print(f'z pattern   : {z_pattern}')
    print('─' * 60)

    # ---- read section definitions ------------------------------------------
    sections = load_sections(args.section_transports_yml_path)
    print(f'Sections loaded ({len(sections)}):')
    for sname, sdef in sections.items():
        comp = infer_component(sname, **sdef)
        print(f'  {sname:30s}  {comp}  '
              f'lon=[{sdef["lon1"]}, {sdef["lon2"]}]  '
              f'lat=[{sdef["lat1"]}, {sdef["lat2"]}]')
    print('─' * 60)

    # ---- optional dask cluster ---------------------------------------------
    nw = args.number_of_workers
    if nw > 1:
        try:
            from ncar_jobqueue import NCARCluster
            from dask.distributed import Client
            cluster = NCARCluster()
            cluster.scale(nw)
            client  = Client(cluster)
            print(f'Dask cluster started with {nw} workers.')
        except Exception as e:
            print(f'Warning: could not start Dask cluster ({e}). Running serially.')

    # ---- open z files ------------------------------------------------------
    files = sorted(glob.glob(OUTDIR + z_pattern))
    if not files:
        sys.exit(f'ERROR: no files found matching {OUTDIR + z_pattern}')
    print(f'Opening {len(files)} z files ...')

    # Decide which variables to keep
    need_umo = any(
        infer_component(n, **d) == 'umo' for n, d in sections.items())
    need_vmo = any(
        infer_component(n, **d) == 'vmo' for n, d in sections.items())
    keep_vars = []
    if need_umo:
        keep_vars.append('umo')
    if need_vmo:
        keep_vars.append('vmo')

    def preprocess(ds):
        return ds[keep_vars]

    t0 = datetime.now()
    ds = xr.open_mfdataset(
        files,
        parallel=(nw > 1),
        preprocess=preprocess,
        combine='by_coords',
    )
    ds = ds.sel(time=slice(start_date, end_date))
    print(f'Dataset opened in {datetime.now()-t0}  |  {ds.time.size} time steps')

    # ---- compute transports ------------------------------------------------
    transport_arrays = {}
    for sname, sdef in sections.items():
        comp = infer_component(sname, **sdef)
        print(f'Computing transport for "{sname}" ({comp}) ...')
        t0 = datetime.now()

        ts = extract_transport(
            ds, sname,
            lon1=sdef['lon1'], lon2=sdef['lon2'],
            lat1=sdef['lat1'], lat2=sdef['lat2'],
            component=comp,
            debug=args.debug,
        ).compute()   # trigger dask computation once per section

        mean_sv = float(ts.mean())
        print(f'  Done ({datetime.now()-t0})  |  mean = {mean_sv:.2f} Sv')
        transport_arrays[sname] = ts

    # ---- assemble output dataset -------------------------------------------
    # Build a 2-D DataArray: (sections, time)
    section_names = list(transport_arrays.keys())
    time_coord    = transport_arrays[section_names[0]].time

    data_matrix = np.full((len(section_names), time_coord.size), np.nan, dtype=np.float32)
    for i, sname in enumerate(section_names):
        data_matrix[i, :] = transport_arrays[sname].values

    transport_da = xr.DataArray(
        data_matrix,
        dims=['sections', 'time'],
        coords={
            'sections': section_names,
            'time':     time_coord,
        },
        attrs={
            'units':     'Sv',
            'long_name': 'Volume transport',
        },
    )

    out_ds = xr.Dataset({'transport': transport_da})

    # add per-section metadata as global attributes for reference
    for sname, sdef in sections.items():
        comp = infer_component(sname, **sdef)
        prefix = sname.replace(' ', '_')
        out_ds.attrs[f'{prefix}_component'] = comp
        out_ds.attrs[f'{prefix}_lon']        = f"{sdef['lon1']}, {sdef['lon2']}"
        out_ds.attrs[f'{prefix}_lat']        = f"{sdef['lat1']}, {sdef['lat2']}"

    add_global_attrs(out_ds, {
        'description': 'Monthly volume transport time series for custom sections',
        'casename':    casename,
        'start_date':  start_date,
        'end_date':    end_date,
        'rho_0':       f'{RHO_0} kg/m3 (used for kg/s -> Sv conversion)',
    })

    # ---- write netCDF ------------------------------------------------------
    outfile = f'ncfiles/{casename}_section_transports.nc'
    out_ds.to_netcdf(outfile)
    print('─' * 60)
    print(f'Saved: {outfile}')
    print('─' * 60)


if __name__ == '__main__':
    main()
