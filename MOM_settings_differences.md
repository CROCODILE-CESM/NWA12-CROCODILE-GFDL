# Ocean configuration differences

This compares every parameter recorded in `MOM_parameter_doc.all.GFDL` (NWA12-GFDL) and `MOM_parameter_doc.all.NCAR` (NWA12-NCAR). The table is organized by MOM6 module.

MOM6 only prints a parameter into `MOM_parameter_doc.all` if the code actually calls `get_param(...)` for it during that run, so a parameter missing from one file was never queried.

Notes:
- `NCAR` = `<--------` means the NCAR value is identical to the GFDL value shown in the same row;
- **`not found (module X inactive)`** — the parameter's module never appears anywhere in that run's `.all` doc at all;
- **`not found (module X active — parameter not queried)`** — the module *is* active in that run (its block does appear), but this specific parameter wasn't read.

Total: 786 unique parameters across 61 modules.

### `MOM`

| Parameter | GFDL | NCAR |
|---|---|---|
| `SPLIT` | `True` | <-------- |
| `SPLIT_RK2B` | *not found* (module `MOM` active — parameter not queried) | `False` |
| `CALC_RHO_FOR_SEA_LEVEL` | `False` | <-------- |
| `ENABLE_THERMODYNAMICS` | `True` | <-------- |
| `USE_EOS` | `True` | <-------- |
| `DIABATIC_FIRST` | `True` | <-------- |
| `USE_CONTEMP_ABSSAL` | `False` | <-------- |
| `ADIABATIC` | `False` | <-------- |
| `DO_DYNAMICS` | `True` | <-------- |
| `OFFLINE_TRACER_MODE` | `False` | <-------- |
| `USE_REGRIDDING` | `True` | <-------- |
| `REMAP_UV_USING_OLD_ALG` | `False` | <-------- |
| `REMAP_AUXILIARY_VARS` | `False` | <-------- |
| `BULKMIXEDLAYER` | `False` | <-------- |
| `USE_POROUS_BARRIER` | `True` | `False` |
| `BATHYMETRY_AT_VEL` | `False` | <-------- |
| `ENABLE_BUGS_BY_DEFAULT` | *not found* (module `MOM` active — parameter not queried) | `True` |
| `DT` | `600.0` | `450.0` |
| `DT_THERM` | `1200.0` | `1800.0` |
| `THERMO_SPANS_COUPLING` | `False` | <-------- |
| `DT_TRACER_ADVECT` | *not found* (module `MOM` active — parameter not queried) | `1800.0` |
| `TRADV_SPANS_COUPLING` | *not found* (module `MOM` active — parameter not queried) | `False` |
| `THICKNESSDIFFUSE` | `False` | <-------- |
| `APPLY_INTERFACE_FILTER` | `False` | <-------- |
| `HMIX_SFC_PROP` | `1.0` | <-------- |
| `HMIX_UV_SFC_PROP` | `0.0` | <-------- |
| `HFREEZE` | `-1.0` | <-------- |
| `INTERPOLATE_P_SURF` | `False` | <-------- |
| `DTBT_RESET_PERIOD` | `1200.0` | `0.0` |
| `FRAZIL` | `True` | <-------- |
| `DO_GEOTHERMAL` | `True` | `False` |
| `BOUND_SALINITY` | `True` | <-------- |
| `MIN_SALINITY` | `0.0` | <-------- |
| `SALINITY_UNDERFLOW` | `0.0` | <-------- |
| `TEMPERATURE_UNDERFLOW` | `0.0` | <-------- |
| `C_P` | `3992.0` | <-------- |
| `USE_PSURF_IN_EOS` | `True` | <-------- |
| `P_REF` | `2.0E+07` | <-------- |
| `FIRST_DIRECTION` | `0` | <-------- |
| `ALTERNATE_FIRST_DIRECTION` | `False` | <-------- |
| `CHECK_BAD_SURFACE_VALS` | `False` | `True` |
| `BAD_VAL_SSH_MAX` | *not found* (module `MOM` active — parameter not queried) | `50.0` |
| `BAD_VAL_SSS_MAX` | *not found* (module `MOM` active — parameter not queried) | `45.0` |
| `BAD_VAL_SST_MAX` | *not found* (module `MOM` active — parameter not queried) | `65.0` |
| `BAD_VAL_SST_MIN` | *not found* (module `MOM` active — parameter not queried) | `-3.0` |
| `BAD_VAL_COLUMN_THICKNESS` | *not found* (module `MOM` active — parameter not queried) | `0.0` |
| `DEFAULT_ANSWER_DATE` | `99991231` | <-------- |
| `DEFAULT_2018_ANSWERS` | `False` | *not found* (module `MOM` active — parameter not queried) |
| `SURFACE_2018_ANSWERS` | `False` | *not found* (module `MOM` active — parameter not queried) |
| `SURFACE_ANSWER_DATE` | `99991231` | <-------- |
| `USE_DIABATIC_TIME_BUG` | `False` | *not found* (module `MOM` active — parameter not queried) |
| `SAVE_INITIAL_CONDS` | `False` | <-------- |
| `IC_OUTPUT_FILE` | `MOM_IC` | `oleanderNWA12_1993-2026.mom6.ic.1993-01-01.nc` |
| `WRITE_GEOM` | `0` | `1` |
| `GEOM_FILE` | *not found* (module `MOM` active — parameter not queried) | `oleanderNWA12_1993-2026.mom6.h.ocean_geometry.nc` |
| `USE_DBCLIENT` | `False` | <-------- |
| `USE_PARTICLES` | `False` | <-------- |
| `USE_UH_PARTICLES` | *not found* (module `MOM` active — parameter not queried) | `False` |
| `ENSEMBLE_OCEAN` | `False` | <-------- |
| `HOMOGENIZE_FORCINGS` | `False` | <-------- |

### `MOM_domains`

| Parameter | GFDL | NCAR |
|---|---|---|
| `REENTRANT_X` | `False` | <-------- |
| `REENTRANT_Y` | `False` | <-------- |
| `TRIPOLAR_N` | `False` | <-------- |
| `NIGLOBAL` | `775` | `740` |
| `NJGLOBAL` | `845` | `780` |
| `NIHALO` | `4` | <-------- |
| `NJHALO` | `4` | <-------- |

### `MOM_grid`

| Parameter | GFDL | NCAR |
|---|---|---|
| `REFERENCE_HEIGHT` | `0.0` | <-------- |

### `MOM_fixed_initialization`

| Parameter | GFDL | NCAR |
|---|---|---|
| `INPUTDIR` | `INPUT` | `/glade/work/emilanese/croc_input/oleanderNWA12_1993-2026/ocnice` |

### `MOM_grid_init`

| Parameter | GFDL | NCAR |
|---|---|---|
| `GRID_CONFIG` | `mosaic` | <-------- |
| `GRID_FILE` | `ocean_hgrid.nc` | `ocean_hgrid_ocean_hgrid_a140db.nc` |
| `USE_TRIPOLAR_GEOLONB_BUG` | `False` | <-------- |
| `RAD_EARTH` | `6.378E+06` | `6.37122E+06` |
| `TOPO_CONFIG` | `file` | <-------- |
| `TOPO_FILE` | `ocean_topog.nc` | `ocean_topog_ocean_hgrid_a140db.nc` |
| `TOPO_VARNAME` | `depth` | <-------- |
| `TOPO_EDITS_FILE` | *(empty)* | <-------- |
| `ALLOW_LANDMASK_CHANGES` | `False` | <-------- |
| `MINIMUM_DEPTH` | `4.0` | `0.0` |
| `MASKING_DEPTH` | `1.0` | `-9999.0` |
| `MAXIMUM_DEPTH` | `6500.0` | `8369.66015625` |

### `MOM_open_boundary`

| Parameter | GFDL | NCAR |
|---|---|---|
| `OBC_NUMBER_OF_SEGMENTS` | `3` | `4` |
| `OBC_ZERO_VORTICITY` | `False` | <-------- |
| `OBC_FREESLIP_VORTICITY` | `False` | <-------- |
| `OBC_COMPUTED_VORTICITY` | `True` | <-------- |
| `OBC_SPECIFIED_VORTICITY` | `False` | <-------- |
| `OBC_ZERO_STRAIN` | `False` | <-------- |
| `OBC_FREESLIP_STRAIN` | `False` | <-------- |
| `OBC_COMPUTED_STRAIN` | `True` | <-------- |
| `OBC_SPECIFIED_STRAIN` | `False` | <-------- |
| `OBC_ZERO_BIHARMONIC` | `True` | <-------- |
| `MASK_OUTSIDE_OBCS` | `False` | <-------- |
| `RAMP_OBCS` | `False` | <-------- |
| `OBC_RAMP_TIMESCALE` | `2.0` | <-------- |
| `OBC_TIDE_N_CONSTITUENTS` | `10` | `1` |
| `EXTERIOR_OBC_BUG` | *not found* (module `MOM_open_boundary` active — parameter not queried) | `True` |
| `OBC_HOR_INDEXING_BUG` | *not found* (module `MOM_open_boundary` active — parameter not queried) | `True` |
| `OBC_SEGMENT_001` | `J=0,I=0:N,FLATHER,ORLANSKI,NUDGED,ORLANSKI_TAN,NUDGED_TAN` | `J=N,I=N:0,FLATHER,ORLANSKI,NUDGED,ORLANSKI_TAN,NUDGED_TAN` |
| `OBC_SEGMENT_001_VELOCITY_NUDGING_TIMESCALES` | `3.0, 360.0` | `0.3, 360.0` |
| `OBC_SEGMENT_002` | `J=N,I=N:0,FLATHER,ORLANSKI,NUDGED,ORLANSKI_TAN,NUDGED_TAN` | `J=0,I=0:N,FLATHER,ORLANSKI,NUDGED,ORLANSKI_TAN,NUDGED_TAN` |
| `OBC_SEGMENT_002_VELOCITY_NUDGING_TIMESCALES` | `3.0, 360.0` | `0.3, 360.0` |
| `OBC_SEGMENT_003` | `I=N,J=0:N,FLATHER,ORLANSKI,NUDGED,ORLANSKI_TAN,NUDGED_TAN` | <-------- |
| `OBC_SEGMENT_003_VELOCITY_NUDGING_TIMESCALES` | `3.0, 360.0` | `0.3, 360.0` |
| `OBC_SEGMENT_004` | *not found* (module `MOM_open_boundary` active — parameter not queried) | `I=0,J=N:0,FLATHER,ORLANSKI,NUDGED,ORLANSKI_TAN,NUDGED_TAN` |
| `OBC_SEGMENT_004_VELOCITY_NUDGING_TIMESCALES` | *not found* (module `MOM_open_boundary` active — parameter not queried) | `0.3, 360.0` |
| `OBC_RADIATION_MAX` | `1.0` | <-------- |
| `OBC_RAD_VEL_WT` | `0.3` | <-------- |
| `OBC_TRACER_RESERVOIR_LENGTH_SCALE_OUT` | `9000.0` | `3.0E+04` |
| `OBC_TRACER_RESERVOIR_LENGTH_SCALE_IN` | `9000.0` | `3000.0` |
| `OBC_THICKNESS_RESERVOIR_LENGTH_SCALE_OUT` | *not found* (module `MOM_open_boundary` active — parameter not queried) | `0.0` |
| `OBC_THICKNESS_RESERVOIR_LENGTH_SCALE_IN` | *not found* (module `MOM_open_boundary` active — parameter not queried) | `0.0` |
| `OBC_REMAPPING_SCHEME` | *not found* (module `MOM_open_boundary` active — parameter not queried) | `PPM_H4` |
| `BRUSHCUTTER_MODE` | `True` | <-------- |
| `REMAPPING_2018_ANSWERS` | `False` | *not found* (module `MOM_open_boundary` active — parameter not queried) |
| `REMAPPING_ANSWER_DATE` | `99991231` | <-------- |
| `OBC_REMAPPING_USE_OM4_SUBCELLS` | *not found* (module `MOM_open_boundary` active — parameter not queried) | `True` |
| `OBC_TIDE_CONSTITUENTS` | `M2,S2,N2,K2,K1,O1,P1,Q1,MM,MF` | `M2` |
| `OBC_TIDE_ADD_EQ_PHASE` | `True` | *not found* (module `MOM_open_boundary` active — parameter not queried) |
| `OBC_TIDE_ADD_NODAL` | `True` | *not found* (module `MOM_open_boundary` active — parameter not queried) |
| `OBC_TIDE_REF_DATE` | `1993, 1, 1` | *not found* (module `MOM_open_boundary` active — parameter not queried) |
| `OBC_TIDE_NODAL_REF_DATE` | `1993, 7, 2` | *not found* (module `MOM_open_boundary` active — parameter not queried) |
| `TIDE_M2_FREQ` | `1.405189E-04` | <-------- |
| `TIDE_S2_FREQ` | `1.454441E-04` | *not found* (module `MOM_open_boundary` active — parameter not queried) |
| `TIDE_N2_FREQ` | `1.378797E-04` | *not found* (module `MOM_open_boundary` active — parameter not queried) |
| `TIDE_K2_FREQ` | `1.4584234E-04` | *not found* (module `MOM_open_boundary` active — parameter not queried) |
| `TIDE_K1_FREQ` | `7.292117E-05` | *not found* (module `MOM_open_boundary` active — parameter not queried) |
| `TIDE_O1_FREQ` | `6.759774E-05` | *not found* (module `MOM_open_boundary` active — parameter not queried) |
| `TIDE_P1_FREQ` | `7.252295E-05` | *not found* (module `MOM_open_boundary` active — parameter not queried) |
| `TIDE_Q1_FREQ` | `6.495854E-05` | *not found* (module `MOM_open_boundary` active — parameter not queried) |
| `TIDE_MM_FREQ` | `2.6392E-06` | *not found* (module `MOM_open_boundary` active — parameter not queried) |
| `TIDE_MF_FREQ` | `5.3234E-06` | *not found* (module `MOM_open_boundary` active — parameter not queried) |
| `OBC_PROJECTION_BUG` | *not found* (module `MOM_open_boundary` active — parameter not queried) | `True` |
| `CHANNEL_CONFIG` | `none` | <-------- |
| `SUBGRID_TOPO_AT_VEL` | `False` | <-------- |
| `ROTATION` | `2omegasinlat` | <-------- |
| `OMEGA` | `7.2921E-05` | <-------- |
| `GRID_ROTATION_ANGLE_BUGS` | `False` | <-------- |

### `MOM_verticalGrid`

| Parameter | GFDL | NCAR |
|---|---|---|
| `G_EARTH` | `9.8` | <-------- |
| `RHO_0` | `1035.0` | <-------- |
| `BOUSSINESQ` | `True` | <-------- |
| `ANGSTROM` | `1.0E-10` | <-------- |
| `H_TO_M` | `1.0` | <-------- |
| `NK` | `75` | <-------- |

### `MOM_EOS`

| Parameter | GFDL | NCAR |
|---|---|---|
| `EQN_OF_STATE` | `WRIGHT` | `WRIGHT_FULL` |
| `EOS_QUADRATURE` | `False` | <-------- |
| `TFREEZE_FORM` | `LINEAR` | <-------- |
| `TFREEZE_S0_P0` | `0.0` | <-------- |
| `DTFREEZE_DS` | `-0.054` | <-------- |
| `DTFREEZE_DP` | `-7.75E-08` | <-------- |
| `TFREEZE_S_IS_PRACS` | *not found* (module `MOM_EOS` active — parameter not queried) | `True` |
| `TFREEZE_T_IS_POTT` | *not found* (module `MOM_EOS` active — parameter not queried) | `True` |

### `MOM_restart`

| Parameter | GFDL | NCAR |
|---|---|---|
| `PARALLEL_RESTARTFILES` | `False` | `True` |
| `RESTARTFILE` | `MOM.res` | <-------- |
| `MAX_FIELDS` | `500` | `100` |
| `RESTART_CHECKSUMS_REQUIRED` | `True` | `False` |
| `WAVE_INTERFACE_ANSWER_DATE` | `20221231` | *not found* (module `MOM_restart` active — parameter not queried) |
| `LA_DEPTH_RATIO` | `0.2` | *not found* (module `MOM_restart` active — parameter not queried) |
| `LA_DEPTH_MIN` | `0.1` | *not found* (module `MOM_restart` active — parameter not queried) |
| `VISCOSITY_AIR` | `1.0E-06` | *not found* (module `MOM_restart` active — parameter not queried) |
| `VON_KARMAN_WAVES` | `0.4` | *not found* (module `MOM_restart` active — parameter not queried) |
| `RHO_AIR` | `1.225` | *not found* (module `MOM_restart` active — parameter not queried) |
| `WAVE_HEIGHT_SCALE_FACTOR` | `0.0246` | *not found* (module `MOM_restart` active — parameter not queried) |
| `CHARNOCK_MIN` | `0.028` | *not found* (module `MOM_restart` active — parameter not queried) |
| `CHARNOCK_SLOPE_U10` | `0.0017` | *not found* (module `MOM_restart` active — parameter not queried) |
| `CHARNOCK_0_WIND_INTERCEPT` | `-0.005` | *not found* (module `MOM_restart` active — parameter not queried) |
| `ENSEMBLE_APPENDIX_PREFIX` | *not found* (module `MOM_restart` active — parameter not queried) | `.mom6` |
| `RESTART_SYMMETRIC_CHECKSUMS` | *not found* (module `MOM_restart` active — parameter not queried) | `False` |
| `RESTART_UNSIGNED_ZEROS` | *not found* (module `MOM_restart` active — parameter not queried) | `False` |
| `USE_FILTER` | *not found* (module `MOM_restart` active — parameter not queried) | `False` |

### `MOM_tracer_flow_control`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_USER_TRACER_EXAMPLE` | `False` | <-------- |
| `USE_DOME_TRACER` | `False` | <-------- |
| `USE_ISOMIP_TRACER` | `False` | <-------- |
| `USE_RGC_TRACER` | `False` | <-------- |
| `USE_IDEAL_AGE_TRACER` | `False` | <-------- |
| `USE_MARBL_TRACERS` | *not found* (module `MOM_tracer_flow_control` active — parameter not queried) | `False` |
| `USE_REGIONAL_DYES` | `False` | <-------- |
| `USE_OIL_TRACER` | `False` | <-------- |
| `USE_ADVECTION_TEST_TRACER` | `False` | <-------- |
| `USE_OCMIP2_CFC` | `False` | <-------- |
| `USE_CFC_CAP` | `False` | <-------- |
| `USE_generic_tracer` | `True` | `False` |
| `USE_PSEUDO_SALT_TRACER` | `False` | <-------- |
| `USE_BOUNDARY_IMPULSE_TRACER` | `False` | <-------- |
| `USE_DYED_OBC_TRACER` | `False` | <-------- |
| `USE_NW2_TRACERS` | `False` | <-------- |

### `register_MOM_generic_tracer`

| Parameter | GFDL | NCAR |
|---|---|---|
| `GENERIC_TRACER_IC_FILE` | `bgc_woa_esper_ics_1993_2023-04.nc` | *not found* (module `register_MOM_generic_tracer` inactive) |
| `GENERIC_TRACER_IC_FILE_IS_Z` | `False` | *not found* (module `register_MOM_generic_tracer` inactive) |
| `TRACERS_MAY_REINIT` | `False` | *not found* (module `register_MOM_generic_tracer` inactive) |

### `MOM_boundary_update`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_FILE_OBC` | `False` | <-------- |
| `USE_TIDAL_BAY_OBC` | `False` | <-------- |
| `USE_KELVIN_WAVE_OBC` | `False` | <-------- |
| `USE_SHELFWAVE_OBC` | `False` | <-------- |
| `USE_DYED_CHANNEL_OBC` | `False` | <-------- |

### `segment_tracer_registry_init`

| Parameter | GFDL | NCAR |
|---|---|---|
| `OBC_SEGMENT_001_DATA` | `U=file:uv_001.nc(u),V=file:uv_001.nc(v),SSH=file:zos_001.nc(zos),TEMP=file:thetao_001.nc(thetao),`<br>`SALT=file:so_001.nc(so),Uamp=file:tu_001.nc(uamp),Uphase=file:tu_001.nc(uphase),Vamp=file:tu_001.nc(vamp),`<br>`Vphase=file:tu_001.nc(vphase),SSHamp=file:tz_001.nc(zamp),SSHphase=file:tz_001.nc(zphase)` | `U=file:forcing_obc_segment_001.nc(u),V=file:forcing_obc_segment_001.nc(v),SSH=file:forcing_obc_segment_001.nc(eta),`<br>`TEMP=file:forcing_obc_segment_001.nc(temp),SALT=file:forcing_obc_segment_001.nc(salt),`<br>`Uamp=file:tu_segment_001.nc(uamp),Uphase=file:tu_segment_001.nc(uphase),Vamp=file:tu_segment_001.nc(vamp),`<br>`Vphase=file:tu_segment_001.nc(vphase),SSHamp=file:tz_segment_001.nc(zamp),SSHphase=file:tz_segment_001.nc(zphase)` |
| `OBC_SEGMENT_002_DATA` | `U=file:uv_002.nc(u),V=file:uv_002.nc(v),SSH=file:zos_002.nc(zos),TEMP=file:thetao_002.nc(thetao),`<br>`SALT=file:so_002.nc(so),Uamp=file:tu_002.nc(uamp),Uphase=file:tu_002.nc(uphase),Vamp=file:tu_002.nc(vamp),`<br>`Vphase=file:tu_002.nc(vphase),SSHamp=file:tz_002.nc(zamp),SSHphase=file:tz_002.nc(zphase)` | `U=file:forcing_obc_segment_002.nc(u),V=file:forcing_obc_segment_002.nc(v),SSH=file:forcing_obc_segment_002.nc(eta),`<br>`TEMP=file:forcing_obc_segment_002.nc(temp),SALT=file:forcing_obc_segment_002.nc(salt),`<br>`Uamp=file:tu_segment_002.nc(uamp),Uphase=file:tu_segment_002.nc(uphase),Vamp=file:tu_segment_002.nc(vamp),`<br>`Vphase=file:tu_segment_002.nc(vphase),SSHamp=file:tz_segment_002.nc(zamp),SSHphase=file:tz_segment_002.nc(zphase)` |
| `OBC_SEGMENT_003_DATA` | `U=file:uv_003.nc(u),V=file:uv_003.nc(v),SSH=file:zos_003.nc(zos),TEMP=file:thetao_003.nc(thetao),`<br>`SALT=file:so_003.nc(so),Uamp=file:tu_003.nc(uamp),Uphase=file:tu_003.nc(uphase),Vamp=file:tu_003.nc(vamp),`<br>`Vphase=file:tu_003.nc(vphase),SSHamp=file:tz_003.nc(zamp),SSHphase=file:tz_003.nc(zphase)` | `U=file:forcing_obc_segment_003.nc(u),V=file:forcing_obc_segment_003.nc(v),SSH=file:forcing_obc_segment_003.nc(eta),`<br>`TEMP=file:forcing_obc_segment_003.nc(temp),SALT=file:forcing_obc_segment_003.nc(salt),`<br>`Uamp=file:tu_segment_003.nc(uamp),Uphase=file:tu_segment_003.nc(uphase),Vamp=file:tu_segment_003.nc(vamp),`<br>`Vphase=file:tu_segment_003.nc(vphase),SSHamp=file:tz_segment_003.nc(zamp),SSHphase=file:tz_segment_003.nc(zphase)` |
| `OBC_SEGMENT_004_DATA` | *not found* (module `segment_tracer_registry_init` inactive) | `U=file:forcing_obc_segment_004.nc(u),V=file:forcing_obc_segment_004.nc(v),SSH=file:forcing_obc_segment_004.nc(eta),`<br>`TEMP=file:forcing_obc_segment_004.nc(temp),SALT=file:forcing_obc_segment_004.nc(salt),`<br>`Uamp=file:tu_segment_004.nc(uamp),Uphase=file:tu_segment_004.nc(uphase),Vamp=file:tu_segment_004.nc(vamp),`<br>`Vphase=file:tu_segment_004.nc(vphase),SSHamp=file:tz_segment_004.nc(zamp),SSHphase=file:tz_segment_004.nc(zphase)` |

### `MOM_coord_initialization`

| Parameter | GFDL | NCAR |
|---|---|---|
| `COORD_CONFIG` | `ALE` | `none` |
| `GFS` | `9.8` | <-------- |
| `LIGHTEST_DENSITY` | *not found* (module `MOM_coord_initialization` active — parameter not queried) | `1035.0` |
| `REGRIDDING_COORDINATE_MODE` | `Z*` | <-------- |
| `REGRIDDING_COORDINATE_UNITS` | `m` | <-------- |
| `ALE_COORDINATE_CONFIG` | `FILE:vgrid_75_2m.nc,dz` | `FILE:ocean_vgrid_ocean_hgrid_a140db.nc` |
| `MIN_THICKNESS` | `1.0E-06` | <-------- |
| `REMAPPING_SCHEME` | `PPM_H4` | <-------- |
| `VELOCITY_REMAPPING_SCHEME` | `PPM_H4` | <-------- |
| `FATAL_CHECK_RECONSTRUCTIONS` | `False` | <-------- |
| `FATAL_CHECK_REMAPPING` | `False` | <-------- |
| `REMAP_BOUND_INTERMEDIATE_VALUES` | `False` | <-------- |
| `REMAP_BOUNDARY_EXTRAP` | `False` | <-------- |
| `INIT_BOUNDARY_EXTRAP` | *not found* (module `MOM_coord_initialization` active — parameter not queried) | `False` |
| `REMAPPING_USE_OM4_SUBCELLS` | *not found* (module `MOM_coord_initialization` active — parameter not queried) | `True` |
| `PARTIAL_CELL_VELOCITY_REMAP` | `False` | <-------- |
| `REMAP_AFTER_INITIALIZATION` | `True` | <-------- |
| `REGRID_TIME_SCALE` | `0.0` | <-------- |
| `REGRID_FILTER_SHALLOW_DEPTH` | `0.0` | <-------- |
| `REGRID_FILTER_DEEP_DEPTH` | `0.0` | <-------- |
| `REMAP_VEL_MASK_BBL_THICK` | `-0.001` | <-------- |
| `REMAP_VEL_CONSERVE_KE` | *not found* (module `MOM_coord_initialization` active — parameter not queried) | `False` |

### `MOM_state_initialization`

| Parameter | GFDL | NCAR |
|---|---|---|
| `FATAL_INCONSISTENT_RESTART_TIME` | `False` | <-------- |
| `INIT_LAYERS_FROM_Z_FILE` | `False` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `THICKNESS_CONFIG` | `coord` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `TS_CONFIG` | `file` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `TS_FILE` | `glorys_ic_1993-01-01.nc` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `TEMP_IC_VAR` | `temp` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `SALT_IC_VAR` | `salt` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `SALT_FILE` | `glorys_ic_1993-01-01.nc` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `DEPRESS_INITIAL_SURFACE` | `True` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `TRIM_IC_FOR_P_SURF` | `False` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `VELOCITY_CONFIG` | `file` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `VELOCITY_FILE` | `glorys_ic_1993-01-01.nc` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `Z_INIT_REMAPPING_USE_OM4_SUBCELLS` | *not found* (module `MOM_state_initialization` active — parameter not queried) | `True` |
| `U_IC_VAR` | `u` | <-------- |
| `V_IC_VAR` | `v` | <-------- |
| `CONVERT_THICKNESS_UNITS` | `False` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `SURFACE_HEIGHT_IC_FILE` | `glorys_ic_1993-01-01.nc` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `SURFACE_HEIGHT_IC_VAR` | `ssh` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `SURFACE_HEIGHT_IC_SCALE` | `1.0` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `REGRID_ACCELERATE_INIT` | `False` | *not found* (module `MOM_state_initialization` active — parameter not queried) |
| `ODA_INCUPD` | `False` | <-------- |
| `SPONGE` | `False` | <-------- |
| `OBC_RESERVOIR_INIT_BUG` | *not found* (module `MOM_state_initialization` active — parameter not queried) | `True` |
| `OBC_USER_CONFIG` | `none` | <-------- |

### `MOM_diag_mediator`

| Parameter | GFDL | NCAR |
|---|---|---|
| `NUM_DIAG_COORDS` | `1` | `2` |
| `USE_GRID_SPACE_DIAGNOSTIC_AXES` | `False` | *not found* (module `MOM_diag_mediator` active — parameter not queried) |
| `DIAG_REMAPPING_USE_OM4_SUBCELLS` | *not found* (module `MOM_diag_mediator` active — parameter not queried) | `True` |
| `USE_INDEX_DIAGNOSTIC_AXES` | *not found* (module `MOM_diag_mediator` active — parameter not queried) | `False` |
| `DIAG_COORDS` | `z Z ZSTAR` | `z ZA ZSTAR", "ole ZB ZSTAR` |
| `DIAG_MISVAL` | `1.0E+20` | <-------- |
| `DIAG_AS_CHKSUM` | `False` | <-------- |
| `AVAILABLE_DIAGS_FILE` | `available_diags.000000` | <-------- |
| `DIAG_COORD_DEF_Z` | `FILE:diag_dz.nc,dz` | *not found* (module `MOM_diag_mediator` active — parameter not queried) |
| `DIAG_COORD_DEF_ZA` | *not found* (module `MOM_diag_mediator` active — parameter not queried) | `UNIFORM` |
| `DIAG_COORD_DEF_ZB` | *not found* (module `MOM_diag_mediator` active — parameter not queried) | `UNIFORM:100,10.` |

### `MOM_MEKE`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_MEKE` | `False` | <-------- |

### `MOM_lateral_mixing_coeffs`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_VARIABLE_MIXING` | `True` | <-------- |
| `USE_VISBECK` | `False` | <-------- |
| `RESOLN_SCALED_KH` | `False` | <-------- |
| `DEPTH_SCALED_KHTH` | `False` | <-------- |
| `RESOLN_SCALED_KHTH` | `False` | <-------- |
| `RESOLN_SCALED_KHTR` | `False` | <-------- |
| `RESOLN_USE_EBT` | `False` | <-------- |
| `BACKSCAT_EBT_POWER` | *not found* (module `MOM_lateral_mixing_coeffs` active — parameter not queried) | `0.0` |
| `BS_USE_SQG_STRUCT` | *not found* (module `MOM_lateral_mixing_coeffs` active — parameter not queried) | `False` |
| `KHTH_USE_EBT_STRUCT` | `False` | <-------- |
| `KHTH_USE_SQG_STRUCT` | *not found* (module `MOM_lateral_mixing_coeffs` active — parameter not queried) | `False` |
| `KHTR_USE_EBT_STRUCT` | *not found* (module `MOM_lateral_mixing_coeffs` active — parameter not queried) | `False` |
| `KHTR_USE_SQG_STRUCT` | *not found* (module `MOM_lateral_mixing_coeffs` active — parameter not queried) | `False` |
| `KD_GL90_USE_EBT_STRUCT` | `False` | <-------- |
| `KD_GL90_USE_SQG_STRUCT` | *not found* (module `MOM_lateral_mixing_coeffs` active — parameter not queried) | `False` |
| `KHTH_SLOPE_CFF` | `0.0` | <-------- |
| `KHTR_SLOPE_CFF` | `0.0` | <-------- |
| `USE_STORED_SLOPES` | `True` | <-------- |
| `VERY_SMALL_FREQUENCY` | `1.0E-17` | <-------- |
| `USE_STANLEY_ISO` | `False` | <-------- |
| `MIXING_COEFS_OBC_BUG` | *not found* (module `MOM_lateral_mixing_coeffs` active — parameter not queried) | `True` |
| `RESOLN_FUNCTION_OBC_BUG` | *not found* (module `MOM_lateral_mixing_coeffs` active — parameter not queried) | `True` |
| `KD_SMOOTH` | `1.0E-06` | <-------- |
| `INTERNAL_WAVE_SPEED_TOL` | `0.001` | <-------- |
| `INTERNAL_WAVE_SPEED_MIN` | `0.0` | <-------- |
| `INTERNAL_WAVE_SPEED_BETTER_EST` | `True` | <-------- |
| `EBT_REMAPPING_USE_OM4_SUBCELLS` | *not found* (module `MOM_lateral_mixing_coeffs` active — parameter not queried) | `True` |
| `USE_QG_LEITH_GM` | `False` | <-------- |

### `MOM_set_visc`

| Parameter | GFDL | NCAR |
|---|---|---|
| `SET_VISC_2018_ANSWERS` | `False` | *not found* (module `MOM_set_visc` active — parameter not queried) |
| `SET_VISC_ANSWER_DATE` | `99991231` | <-------- |
| `BOTTOMDRAGLAW` | `True` | <-------- |
| `DRAG_AS_BODY_FORCE` | `False` | <-------- |
| `CHANNEL_DRAG` | `True` | <-------- |
| `LINEAR_DRAG` | `False` | <-------- |
| `PRANDTL_TURB` | `1.25` | *not found* (module `MOM_set_visc` active — parameter not queried) |
| `DYNAMIC_VISCOUS_ML` | `False` | <-------- |
| `HBBL` | `10.0` | <-------- |
| `CDRAG` | `0.003` | <-------- |
| `BBL_USE_TIDAL_BG` | `False` | <-------- |
| `DRAG_BG_VEL` | `0.0` | <-------- |
| `BBL_USE_EOS` | `True` | <-------- |
| `BBL_THICK_MIN` | `0.1` | <-------- |
| `HTBL_SHELF_MIN` | `0.1` | <-------- |
| `HTBL_SHELF` | `10.0` | <-------- |
| `KV` | `1.0E-06` | <-------- |
| `KV_BBL_MIN` | `1.0E-06` | <-------- |
| `KV_TBL_MIN` | `1.0E-06` | <-------- |
| `CORRECT_BBL_BOUNDS` | `False` | <-------- |
| `SMAG_CONST_CHANNEL` | `0.15` | <-------- |
| `TRIG_CHANNEL_DRAG_WIDTHS` | *not found* (module `MOM_set_visc` active — parameter not queried) | `True` |
| `CHANNEL_DRAG_MAX_BBL_THICK` | `5.0` | <-------- |

### `MOM_thickness_diffuse`

| Parameter | GFDL | NCAR |
|---|---|---|
| `KHTH` | `0.0` | <-------- |
| `READ_KHTH` | `False` | <-------- |
| `KHTH_MIN` | `0.0` | <-------- |
| `KHTH_MAX` | `0.0` | <-------- |
| `KHTH_MAX_CFL` | `0.1` | <-------- |
| `KH_ETA_CONST` | `0.0` | <-------- |
| `KH_ETA_VEL_SCALE` | `0.0` | <-------- |
| `DETANGLE_INTERFACES` | `False` | <-------- |
| `KHTH_SLOPE_MAX` | `0.01` | <-------- |
| `KHTH_USE_FGNV_STREAMFUNCTION` | `False` | <-------- |
| `USE_STANLEY_GM` | `False` | <-------- |
| `MEKE_GM_SRC_ALT` | `False` | <-------- |
| `MEKE_GEOMETRIC` | `False` | <-------- |
| `USE_KH_IN_MEKE` | `False` | *not found* (module `MOM_thickness_diffuse` active — parameter not queried) |
| `USE_GME` | `False` | <-------- |
| `USE_GM_WORK_BUG` | `False` | <-------- |

### `MOM_porous_barriers`

| Parameter | GFDL | NCAR |
|---|---|---|
| `PORBAR_ANSWER_DATE` | `99991231` | *not found* (module `MOM_porous_barriers` inactive) |
| `PORBAR_MASKING_DEPTH` | `0.0` | *not found* (module `MOM_porous_barriers` inactive) |
| `PORBAR_ETA_INTERP` | `MAX` | *not found* (module `MOM_porous_barriers` inactive) |

### `MOM_stoch_eos`

| Parameter | GFDL | NCAR |
|---|---|---|
| `STOCH_EOS` | `False` | <-------- |
| `STANLEY_COEFF` | `-1.0` | <-------- |

### `MOM_dynamics_split_RK2`

| Parameter | GFDL | NCAR |
|---|---|---|
| `TIDES` | `True` | <-------- |
| `CALCULATE_SAL` | *not found* (module `MOM_dynamics_split_RK2` active — parameter not queried) | `True` |
| `USE_HA` | *not found* (module `MOM_dynamics_split_RK2` active — parameter not queried) | `False` |
| `BE` | `0.6` | <-------- |
| `BEGW` | `0.0` | <-------- |
| `SET_DTBT_USE_BT_CONT` | *not found* (module `MOM_dynamics_split_RK2` active — parameter not queried) | `False` |
| `SPLIT_BOTTOM_STRESS` | `False` | <-------- |
| `BT_USE_LAYER_FLUXES` | `True` | <-------- |
| `BT_ADJ_CORR_MASS_SRC` | *not found* (module `MOM_dynamics_split_RK2` active — parameter not queried) | `True` |
| `STORE_CORIOLIS_ACCEL` | `True` | <-------- |
| `FPMIX` | *not found* (module `MOM_dynamics_split_RK2` active — parameter not queried) | `False` |
| `VISC_REM_BUG` | *not found* (module `MOM_dynamics_split_RK2` active — parameter not queried) | `False` |
| `VISC_REM_TIMESTEP_BUG` | *not found* (module `MOM_dynamics_split_RK2` active — parameter not queried) | `False` |

### `MOM_continuity`

| Parameter | GFDL | NCAR |
|---|---|---|
| `CONTINUITY_SCHEME` | `PPM` | *not found* (module `MOM_continuity` inactive) |

### `MOM_continuity_PPM`

| Parameter | GFDL | NCAR |
|---|---|---|
| `MONOTONIC_CONTINUITY` | `False` | <-------- |
| `SIMPLE_2ND_PPM_CONTINUITY` | `False` | <-------- |
| `UPWIND_1ST_CONTINUITY` | `False` | <-------- |
| `ETA_TOLERANCE` | `1.0E-06` | <-------- |
| `VELOCITY_TOLERANCE` | `3.0E+08` | <-------- |
| `CONT_PPM_AGGRESS_ADJUST` | `False` | <-------- |
| `CONT_PPM_VOLUME_BASED_CFL` | `False` | <-------- |
| `CONTINUITY_CFL_LIMIT` | `0.5` | <-------- |
| `CONT_PPM_BETTER_ITER` | `True` | <-------- |
| `CONT_PPM_USE_VISC_REM_MAX` | `True` | <-------- |
| `CONT_PPM_MARGINAL_FACE_AREAS` | `True` | <-------- |

### `MOM_CoriolisAdv`

| Parameter | GFDL | NCAR |
|---|---|---|
| `NOSLIP` | `False` | <-------- |
| `CORIOLIS_EN_DIS` | `True` | <-------- |
| `CORIOLIS_SCHEME` | `SADOURNY75_ENERGY` | <-------- |
| `BOUND_CORIOLIS` | `False` | `True` |
| `KE_SCHEME` | `KE_ARAKAWA` | <-------- |
| `PV_ADV_SCHEME` | `PV_ADV_CENTERED` | <-------- |

### `MOM_self_attr_load`

| Parameter | GFDL | NCAR |
|---|---|---|
| `SAL_USE_BPA` | *not found* (module `MOM_self_attr_load` inactive) | `False` |
| `SAL_SCALAR_APPROX` | *not found* (module `MOM_self_attr_load` inactive) | `True` |
| `SAL_SCALAR_VALUE` | *not found* (module `MOM_self_attr_load` inactive) | `0.0` |
| `SAL_HARMONICS` | *not found* (module `MOM_self_attr_load` inactive) | `False` |

### `MOM_tidal_forcing`

| Parameter | GFDL | NCAR |
|---|---|---|
| `TIDE_M2` | `True` | <-------- |
| `TIDE_S2` | `True` | `False` |
| `TIDE_N2` | `True` | `False` |
| `TIDE_K2` | `True` | `False` |
| `TIDE_K1` | `True` | `False` |
| `TIDE_O1` | `True` | `False` |
| `TIDE_P1` | `True` | `False` |
| `TIDE_Q1` | `True` | `False` |
| `TIDE_MF` | `True` | `False` |
| `TIDE_MM` | `True` | `False` |
| `TIDAL_SAL_FROM_FILE` | `False` | <-------- |
| `USE_PREVIOUS_TIDES` | `False` | <-------- |
| `TIDE_USE_SAL_SCALAR` | `True` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_SAL_SCALAR_VALUE` | `0.01` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDAL_SAL_SHT` | `False` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_REF_DATE` | `1993, 1, 1` | <-------- |
| `TIDE_USE_EQ_PHASE` | `True` | <-------- |
| `TIDE_M2_AMP` | `0.242334` | <-------- |
| `TIDE_M2_PHASE_T0` | `9.347582645568489` | <-------- |
| `TIDE_S2_AMP` | `0.112743` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_S2_PHASE_T0` | `0.0` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_N2_AMP` | `0.046397` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_N2_PHASE_T0` | `11.890182671016415` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_K2_AMP` | `0.030684` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_K2_PHASE_T0` | `9.79682726018515` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_K1_AMP` | `0.141565` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_K1_PHASE_T0` | `6.469209956887472` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_O1_AMP` | `0.100661` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_O1_PHASE_T0` | `2.878372688681016` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_P1_AMP` | `0.046848` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_P1_PHASE_T0` | `-6.469209956887472` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_Q1_AMP` | `0.019273` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_Q1_PHASE_T0` | `5.420972714128944` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_MF_AMP` | `0.042041` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_MF_PHASE_T0` | `0.4492446146166624` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_MM_AMP` | `0.022191` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_MM_PHASE_T0` | `-2.542600025447928` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) |
| `TIDE_ADD_NODAL` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) | `True` |
| `TIDE_NODAL_REF_DATE` | *not found* (module `MOM_tidal_forcing` active — parameter not queried) | `1993, 1, 1` |

### `MOM_PressureForce`

| Parameter | GFDL | NCAR |
|---|---|---|
| `ANALYTIC_FV_PGF` | `True` | <-------- |

### `MOM_PressureForce_FV`

| Parameter | GFDL | NCAR |
|---|---|---|
| `RHO_PGF_REF` | *not found* (module `MOM_PressureForce_FV` active — parameter not queried) | `1035.0` |
| `RHO_PGF_REF_BUG` | *not found* (module `MOM_PressureForce_FV` active — parameter not queried) | `False` |
| `TIDES_ANSWER_DATE` | *not found* (module `MOM_PressureForce_FV` active — parameter not queried) | `99991231` |
| `BOUSSINESQ_SAL_TIDES` | *not found* (module `MOM_PressureForce_FV` active — parameter not queried) | `False` |
| `SSH_IN_EOS_PRESSURE_FOR_PGF` | *not found* (module `MOM_PressureForce_FV` active — parameter not queried) | `False` |
| `MASS_WEIGHT_IN_PRESSURE_GRADIENT` | `True` | <-------- |
| `MASS_WEIGHT_IN_PRESSURE_GRADIENT_TOP` | *not found* (module `MOM_PressureForce_FV` active — parameter not queried) | `True` |
| `MASS_WEIGHT_IN_PGF_VANISHED_ONLY` | *not found* (module `MOM_PressureForce_FV` active — parameter not queried) | `False` |
| `CORRECTION_INTXPA` | *not found* (module `MOM_PressureForce_FV` active — parameter not queried) | `False` |
| `RESET_INTXPA_INTEGRAL` | *not found* (module `MOM_PressureForce_FV` active — parameter not queried) | `False` |
| `RESET_INTXPA_INTEGRAL_FLATTEST` | *not found* (module `MOM_PressureForce_FV` active — parameter not queried) | `False` |
| `USE_INACCURATE_PGF_RHO_ANOM` | `False` | <-------- |
| `RECONSTRUCT_FOR_PRESSURE` | `True` | <-------- |
| `PRESSURE_RECONSTRUCTION_SCHEME` | `1` | <-------- |
| `BOUNDARY_EXTRAPOLATION_PRESSURE` | `True` | <-------- |
| `USE_STANLEY_PGF` | `False` | <-------- |

### `MOM_Zanna_Bolton`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_ZB2020` | *not found* (module `MOM_Zanna_Bolton` inactive) | `False` |

### `MOM_hor_visc`

| Parameter | GFDL | NCAR |
|---|---|---|
| `HOR_VISC_2018_ANSWERS` | `False` | *not found* (module `MOM_hor_visc` active — parameter not queried) |
| `HOR_VISC_ANSWER_DATE` | `99991231` | *not found* (module `MOM_hor_visc` active — parameter not queried) |
| `USE_CIRCULATION_IN_HORVISC` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `False` |
| `USE_CONT_THICKNESS` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `False` |
| `LAPLACIAN` | `False` | `True` |
| `KH` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `0.0` |
| `KH_BG_MIN` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `0.0` |
| `KH_VEL_SCALE` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `0.01` |
| `KH_SIN_LAT` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `0.0` |
| `SMAGORINSKY_KH` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `False` |
| `LEITH_KH` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `False` |
| `BOUND_KH` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `True` |
| `EY24_EBT_BS` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `False` |
| `ANISOTROPIC_VISCOSITY` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `False` |
| `ADD_LES_VISCOSITY` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `False` |
| `BIHARMONIC` | `True` | <-------- |
| `AH` | `0.0` | <-------- |
| `AH_VEL_SCALE` | `0.01` | <-------- |
| `AH_TIME_SCALE` | `0.0` | <-------- |
| `SMAGORINSKY_AH` | `True` | <-------- |
| `LEITH_AH` | `False` | <-------- |
| `USE_LEITHY` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `False` |
| `BOUND_AH` | `True` | <-------- |
| `BETTER_BOUND_AH` | `True` | *not found* (module `MOM_hor_visc` active — parameter not queried) |
| `RE_AH` | `0.0` | <-------- |
| `BACKSCATTER_UNDERBOUND` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `False` |
| `SMAG_BI_CONST` | `0.015` | <-------- |
| `BOUND_CORIOLIS_BIHARM` | `False` | `True` |
| `BOUND_CORIOLIS_VEL` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `6.0` |
| `USE_LAND_MASK_FOR_HVISC` | `True` | <-------- |
| `HORVISC_BOUND_COEF` | `0.8` | <-------- |
| `USE_KH_BG_2D` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `False` |
| `FRICTWORK_BUG` | *not found* (module `MOM_hor_visc` active — parameter not queried) | `False` |

### `MOM_vert_friction`

| Parameter | GFDL | NCAR |
|---|---|---|
| `VERT_FRICTION_2018_ANSWERS` | `False` | *not found* (module `MOM_vert_friction` active — parameter not queried) |
| `VERT_FRICTION_ANSWER_DATE` | `99991231` | <-------- |
| `DIRECT_STRESS` | `True` | <-------- |
| `FIXED_DEPTH_LOTW_ML` | `False` | <-------- |
| `LOTW_VISCOUS_ML_FLOOR` | `False` | <-------- |
| `VON_KARMAN_CONST` | `0.41` | <-------- |
| `HARMONIC_VISC` | `False` | <-------- |
| `HARMONIC_BL_SCALE` | `0.0` | <-------- |
| `HMIX_FIXED` | `0.9` | <-------- |
| `HMIX_STRESS` | `0.9` | <-------- |
| `USE_GL90_IN_SSW` | `False` | <-------- |
| `KV_ML_INVZ2` | `0.0` | <-------- |
| `CFL_BASED_TRUNCATIONS` | `True` | *not found* (module `MOM_vert_friction` active — parameter not queried) |
| `CFL_TRUNCATE` | `0.5` | <-------- |
| `CFL_REPORT` | `0.5` | <-------- |
| `CFL_TRUNCATE_RAMP_TIME` | `0.0` | <-------- |
| `CFL_TRUNCATE_START` | `0.0` | <-------- |
| `STOKES_MIXING_COMBINED` | `False` | <-------- |
| `VEL_UNDERFLOW` | `0.0` | <-------- |

### `MOM_barotropic`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_BT_CONT_TYPE` | `True` | <-------- |
| `INTEGRAL_BT_CONTINUITY` | `False` | <-------- |
| `BOUND_BT_CORRECTION` | `True` | <-------- |
| `BT_CONT_CORR_BOUNDS` | `True` | <-------- |
| `ADJUST_BT_CONT` | `False` | <-------- |
| `GRADUAL_BT_ICS` | `False` | <-------- |
| `BT_USE_VISC_REM_U_UH0` | `False` | <-------- |
| `BT_PROJECT_VELOCITY` | `True` | <-------- |
| `BT_NONLIN_STRESS` | `True` | <-------- |
| `DYNAMIC_SURFACE_PRESSURE` | `True` | <-------- |
| `ICE_LENGTH_DYN_PSURF` | `1.0E+04` | <-------- |
| `DEPTH_MIN_DYN_PSURF` | `1.0E-06` | <-------- |
| `CONST_DYN_PSURF` | `0.9` | <-------- |
| `BT_CORIOLIS_SCALE` | `1.0` | <-------- |
| `BAROTROPIC_2018_ANSWERS` | `False` | *not found* (module `MOM_barotropic` active — parameter not queried) |
| `BAROTROPIC_ANSWER_DATE` | `99991231` | <-------- |
| `BAROTROPIC_TIDAL_SAL_BUG` | `False` | *not found* (module `MOM_barotropic` active — parameter not queried) |
| `VISC_REM_BT_WEIGHT_BUG` | *not found* (module `MOM_barotropic` active — parameter not queried) | `False` |
| `TIDAL_SAL_FLATHER` | *not found* (module `MOM_barotropic` active — parameter not queried) | `False` |
| `SADOURNY` | `False` | <-------- |
| `BT_THICK_SCHEME` | `FROM_BT_CONT` | <-------- |
| `BT_STRONG_DRAG` | `True` | <-------- |
| `RESCALE_STRONG_DRAG` | *not found* (module `MOM_barotropic` active — parameter not queried) | `False` |
| `BT_LINEAR_WAVE_DRAG` | `False` | <-------- |
| `BT_LINEAR_FREQ_DRAG` | *not found* (module `MOM_barotropic` active — parameter not queried) | `False` |
| `CLIP_BT_VELOCITY` | `False` | <-------- |
| `MAXCFL_BT_CONT` | `0.25` | <-------- |
| `DT_BT_FILTER` | `-0.25` | <-------- |
| `G_BT_EXTRA` | `0.0` | <-------- |
| `SSH_EXTRA` | `10.0` | <-------- |
| `LINEARIZED_BT_CORIOLIS` | `False` | <-------- |
| `BEBT` | `0.2` | <-------- |
| `DTBT` | `-0.9` | <-------- |
| `BT_USE_OLD_CORIOLIS_BRACKET_BUG` | `False` | <-------- |
| `MASK_COASTAL_PRESSURE_FORCE` | *not found* (module `MOM_barotropic` active — parameter not queried) | `False` |

### `MOM_mixed_layer_restrat`

| Parameter | GFDL | NCAR |
|---|---|---|
| `MIXEDLAYER_RESTRAT` | `True` | <-------- |
| `USE_STANLEY_ML` | `False` | <-------- |
| `USE_BODNER23` | *not found* (module `MOM_mixed_layer_restrat` active — parameter not queried) | `False` |
| `FOX_KEMPER_ML_RESTRAT_COEF` | `1.0` | <-------- |
| `FOX_KEMPER_ML_RESTRAT_COEF2` | `0.0` | <-------- |
| `MLE_FRONT_LENGTH` | `1500.0` | <-------- |
| `MLE_FRONT_LENGTH_FROM_FILE` | *not found* (module `MOM_mixed_layer_restrat` active — parameter not queried) | `False` |
| `MLE_USE_PBL_MLD` | `True` | <-------- |
| `MLE_MLD_DECAY_TIME` | `2.592E+06` | <-------- |
| `MLE_MLD_DECAY_TIME2` | `0.0` | <-------- |
| `MLE_TAIL_DH` | `0.0` | <-------- |
| `MLE_MLD_STRETCH` | `1.0` | <-------- |
| `KV_RESTRAT` | `0.0` | <-------- |
| `RESTRAT_USTAR_MIN` | `1.45842E-18` | <-------- |

### `MOM_diagnostics`

| Parameter | GFDL | NCAR |
|---|---|---|
| `DIAG_EBT_MONO_N2_COLUMN_FRACTION` | `0.0` | <-------- |
| `DIAG_EBT_MONO_N2_DEPTH` | `-1.0` | <-------- |
| `INTWAVE_REMAPPING_USE_OM4_SUBCELLS` | *not found* (module `MOM_diagnostics` active — parameter not queried) | `True` |

### `MOM_diabatic_driver`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_LEGACY_DIABATIC_DRIVER` | `False` | <-------- |
| `ENERGETICS_SFC_PBL` | `True` | `False` |
| `EPBL_IS_ADDITIVE` | `False` | <-------- |
| `PRANDTL_EPBL` | `1.0` | *not found* (module `MOM_diabatic_driver` active — parameter not queried) |
| `INTERNAL_TIDES` | `False` | <-------- |
| `MASSLESS_MATCH_TARGETS` | `True` | <-------- |
| `AGGREGATE_FW_FORCING` | `True` | <-------- |
| `MIX_BOUNDARY_TRACERS` | `True` | <-------- |
| `MIX_BOUNDARY_TRACER_ALE` | `False` | `True` |
| `KD_MIN_TR` | `1.0E-07` | <-------- |
| `KD_BBL_TR` | `0.0` | <-------- |
| `TRACER_TRIDIAG` | `False` | <-------- |
| `MINIMUM_FORCING_DEPTH` | `0.001` | <-------- |
| `EVAP_CFL_LIMIT` | `0.8` | <-------- |
| `MLD_EN_VALS` | `3*0.0` | `25.0, 2500.0, 2.5E+05` |
| `BMLD_EN_VALS` | *not found* (module `MOM_diabatic_driver` active — parameter not queried) | `25.0, 2500.0, 2.5E+05` |
| `HREF_FOR_MLD` | *not found* (module `MOM_diabatic_driver` active — parameter not queried) | `10.0` |
| `DIAG_MLD_DENSITY_DIFF` | `0.1` | <-------- |
| `DIAG_DEPTH_SUBML_N2` | `50.0` | <-------- |

### `MOM_CVMix_KPP`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_KPP` | `False` | `True` |
| `PASSIVE` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `False` |
| `APPLY_NONLOCAL_TRANSPORT` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `True` |
| `N_SMOOTH` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `3` |
| `DEEPEN_ONLY_VIA_SMOOTHING` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `False` |
| `RI_CRIT` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `0.3` |
| `VON_KARMAN` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `0.4` |
| `ENHANCE_DIFFUSION` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `True` |
| `INTERP_TYPE` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `quadratic` |
| `INTERP_TYPE2` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `LMD94` |
| `STOKES_MOST` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `False` |
| `COMPUTE_EKMAN` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `False` |
| `COMPUTE_MONIN_OBUKHOV` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `False` |
| `CS` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `98.96` |
| `CS2` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `6.32739901508` |
| `DEEP_OBL_OFFSET` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `0.0` |
| `FIXED_OBLDEPTH` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `False` |
| `FIXED_OBLDEPTH_VALUE` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `30.0` |
| `SURF_LAYER_EXTENT` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `0.1` |
| `MINIMUM_OBL_DEPTH` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `0.0` |
| `MINIMUM_VT2` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `1.0E-10` |
| `NLT_SHAPE` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `CVMix` |
| `MATCH_TECHNIQUE` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `MatchGradient` |
| `KPP_ZERO_DIFFUSIVITY` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `False` |
| `KPP_IS_ADDITIVE` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `False` |
| `KPP_SHORTWAVE_METHOD` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `MXL_SW` |
| `CVMix_ZERO_H_WORK_AROUND` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `0.0` |
| `USE_KPP_LT_K` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `False` |
| `STOKES_MIXING` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `False` |
| `USE_KPP_LT_VT2` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `False` |
| `KPP_CVt2` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `1.6` |
| `KPP_ER_Cb` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `0.96` |
| `KPP_ER_Cs` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `0.038` |
| `KPP_ER_Cu` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `0.023` |
| `ANSWER_DATE` | *not found* (module `MOM_CVMix_KPP` active — parameter not queried) | `99991231` |

### `MOM_CVMix_conv`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_CVMix_CONVECTION` | `False` | `True` |
| `PRANDTL_CONV` | *not found* (module `MOM_CVMix_conv` active — parameter not queried) | `1.0` |
| `KD_CONV` | *not found* (module `MOM_CVMix_conv` active — parameter not queried) | `1.0` |
| `BV_SQR_CONV` | *not found* (module `MOM_CVMix_conv` active — parameter not queried) | `0.0` |

### `MOM_geothermal`

| Parameter | GFDL | NCAR |
|---|---|---|
| `GEOTHERMAL_SCALE` | `0.0` | *not found* (module `MOM_geothermal` inactive) |

### `MOM_set_diffusivity`

| Parameter | GFDL | NCAR |
|---|---|---|
| `FLUX_RI_MAX` | `0.2` | <-------- |
| `SET_DIFF_2018_ANSWERS` | `False` | *not found* (module `MOM_set_diffusivity` active — parameter not queried) |
| `SET_DIFF_ANSWER_DATE` | `99991231` | <-------- |

### `MOM_tidal_mixing`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_CVMix_TIDAL` | `False` | <-------- |
| `INT_TIDE_DISSIPATION` | `False` | <-------- |
| `ML_RADIATION` | `False` | <-------- |
| `BBL_EFFIC` | `0.0` | <-------- |
| `BBL_MIXING_MAX_DECAY` | `200.0` | <-------- |
| `BBL_MIXING_AS_MAX` | `False` | <-------- |
| `USE_LOTW_BBL_DIFFUSIVITY` | `False` | <-------- |
| `DZ_BBL_AVG_MIN` | *not found* (module `MOM_tidal_mixing` active — parameter not queried) | `0.0` |
| `SIMPLE_TKE_TO_KD` | `False` | <-------- |

### `MOM_bkgnd_mixing`

| Parameter | GFDL | NCAR |
|---|---|---|
| `KD` | `1.0E-06` | <-------- |
| `KD_MIN` | `2.0E-07` | <-------- |
| `BRYAN_LEWIS_DIFFUSIVITY` | `False` | <-------- |
| `HORIZ_VARYING_BACKGROUND` | `False` | <-------- |
| `PRANDTL_BKGND` | `1.0` | `10.0` |
| `HENYEY_IGW_BACKGROUND` | `False` | <-------- |
| `KD_TANH_LAT_FN` | `False` | <-------- |
| `KD_MAX` | `-1.0` | <-------- |
| `KD_ADD` | `0.0` | <-------- |
| `USER_CHANGE_DIFFUSIVITY` | `False` | <-------- |
| `DISSIPATION_MIN` | `0.0` | <-------- |
| `DISSIPATION_N0` | `0.0` | <-------- |
| `DISSIPATION_N1` | `0.0` | <-------- |
| `DISSIPATION_KD_MIN` | `0.0` | <-------- |
| `DOUBLE_DIFFUSION` | `True` | `False` |
| `MAX_RRHO_SALT_FINGERS` | `2.55` | *not found* (module `MOM_bkgnd_mixing` active — parameter not queried) |
| `MAX_SALT_DIFF_SALT_FINGERS` | `1.0E-04` | *not found* (module `MOM_bkgnd_mixing` active — parameter not queried) |
| `KV_MOLECULAR` | `1.5E-06` | *not found* (module `MOM_bkgnd_mixing` active — parameter not queried) |

### `MOM_kappa_shear`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_JACKSON_PARAM` | `True` | `False` |
| `VERTEX_SHEAR` | `False` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `RINO_CRIT` | `0.25` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `SHEARMIX_RATE` | `0.089` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `MAX_RINO_IT` | `25` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `KD_KAPPA_SHEAR_0` | `1.0E-06` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `VERTEX_SHEAR_THICKNESS_MEAN` | *not found* (module `MOM_kappa_shear` active — parameter not queried) | `False` |
| `KD_SEED_KAPPA_SHEAR` | `1.0` | <-------- |
| `KD_TRUNC_KAPPA_SHEAR` | `1.0E-08` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `FRI_CURVATURE` | `-0.97` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `TKE_N_DECAY_CONST` | `0.24` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `TKE_SHEAR_DECAY_CONST` | `0.14` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `KAPPA_BUOY_SCALE_COEF` | `0.82` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `KAPPA_N_OVER_S_SCALE_COEF2` | `0.0` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `KAPPA_SHEAR_TOL_ERR` | `0.1` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `LZ_RESCALE` | *not found* (module `MOM_kappa_shear` active — parameter not queried) | `1.0` |
| `TKE_BACKGROUND` | `0.0` | <-------- |
| `KAPPA_SHEAR_ELIM_MASSLESS` | `True` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `MAX_KAPPA_SHEAR_IT` | `13` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `KAPPA_SHEAR_MAX_KAP_SRC_CHG` | `10.0` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `KAPPA_SHEAR_ITER_BUG` | `False` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `KAPPA_SHEAR_ALL_LAYER_TKE_BUG` | `False` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |
| `USE_RESTRICTIVE_TOLERANCE_CHECK` | `False` | *not found* (module `MOM_kappa_shear` active — parameter not queried) |

### `MOM_CVMix_shear`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_LMD94` | `False` | `True` |
| `USE_PP81` | `False` | <-------- |
| `NU_ZERO` | *not found* (module `MOM_CVMix_shear` active — parameter not queried) | `0.005` |
| `RI_ZERO` | *not found* (module `MOM_CVMix_shear` active — parameter not queried) | `0.8` |
| `PRANDTL_CVMIX_SHEAR` | *not found* (module `MOM_CVMix_shear` active — parameter not queried) | `1.0` |
| `KPP_EXP` | *not found* (module `MOM_CVMix_shear` active — parameter not queried) | `3.0` |
| `N_SMOOTH_RI` | *not found* (module `MOM_CVMix_shear` active — parameter not queried) | `1` |

### `MOM_CVMix_ddiff`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_CVMIX_DDIFF` | `False` | `True` |
| `STRAT_PARAM_MAX` | *not found* (module `MOM_CVMix_ddiff` active — parameter not queried) | `2.55` |
| `KAPPA_DDIFF_S` | *not found* (module `MOM_CVMix_ddiff` active — parameter not queried) | `1.0E-04` |
| `DDIFF_EXP1` | *not found* (module `MOM_CVMix_ddiff` active — parameter not queried) | `1.0` |
| `DDIFF_EXP2` | *not found* (module `MOM_CVMix_ddiff` active — parameter not queried) | `3.0` |
| `KAPPA_DDIFF_PARAM1` | *not found* (module `MOM_CVMix_ddiff` active — parameter not queried) | `0.909` |
| `KAPPA_DDIFF_PARAM2` | *not found* (module `MOM_CVMix_ddiff` active — parameter not queried) | `4.6` |
| `KAPPA_DDIFF_PARAM3` | *not found* (module `MOM_CVMix_ddiff` active — parameter not queried) | `-0.54` |
| `MOL_DIFF` | *not found* (module `MOM_CVMix_ddiff` active — parameter not queried) | `1.5E-06` |
| `DIFF_CONV_TYPE` | *not found* (module `MOM_CVMix_ddiff` active — parameter not queried) | `MC76` |

### `MOM_diabatic_aux`

| Parameter | GFDL | NCAR |
|---|---|---|
| `RECLAIM_FRAZIL` | `True` | <-------- |
| `SALT_EXTRACTION_LIMIT` | `0.9999` | <-------- |
| `PRESSURE_DEPENDENT_FRAZIL` | `True` | <-------- |
| `IGNORE_FLUXES_OVER_LAND` | `True` | *not found* (module `MOM_diabatic_aux` active — parameter not queried) |
| `DO_RIVERMIX` | `True` | *not found* (module `MOM_diabatic_aux` active — parameter not queried) |
| `RIVERMIX_DEPTH` | `5.0` | *not found* (module `MOM_diabatic_aux` active — parameter not queried) |
| `USE_RIVER_HEAT_CONTENT` | `False` | <-------- |
| `USE_CALVING_HEAT_CONTENT` | `False` | <-------- |
| `DO_BRINE_PLUME` | *not found* (module `MOM_diabatic_aux` active — parameter not queried) | `False` |
| `VAR_PEN_SW` | `True` | `False` |
| `CHL_FROM_FILE` | `False` | *not found* (module `MOM_diabatic_aux` active — parameter not queried) |

### `MOM_energetic_PBL`

| Parameter | GFDL | NCAR |
|---|---|---|
| `ML_OMEGA_FRAC` | `0.001` | *not found* (module `MOM_energetic_PBL` inactive) |
| `EKMAN_SCALE_COEF` | `1.0` | *not found* (module `MOM_energetic_PBL` inactive) |
| `EPBL_2018_ANSWERS` | `False` | *not found* (module `MOM_energetic_PBL` inactive) |
| `EPBL_ANSWER_DATE` | `99991231` | *not found* (module `MOM_energetic_PBL` inactive) |
| `EPBL_ORIGINAL_PE_CALC` | `True` | *not found* (module `MOM_energetic_PBL` inactive) |
| `MKE_TO_TKE_EFFIC` | `0.0` | *not found* (module `MOM_energetic_PBL` inactive) |
| `TKE_DECAY` | `0.001` | *not found* (module `MOM_energetic_PBL` inactive) |
| `EPBL_MSTAR_SCHEME` | `REICHL_H18` | *not found* (module `MOM_energetic_PBL` inactive) |
| `MSTAR_CAP` | `10.0` | *not found* (module `MOM_energetic_PBL` inactive) |
| `RH18_MSTAR_CN1` | `0.275` | *not found* (module `MOM_energetic_PBL` inactive) |
| `RH18_MSTAR_CN2` | `8.0` | *not found* (module `MOM_energetic_PBL` inactive) |
| `RH18_MSTAR_CN3` | `-6.0` | *not found* (module `MOM_energetic_PBL` inactive) |
| `RH18_MSTAR_CS1` | `0.2` | *not found* (module `MOM_energetic_PBL` inactive) |
| `RH18_MSTAR_CS2` | `0.4` | *not found* (module `MOM_energetic_PBL` inactive) |
| `NSTAR` | `0.06` | *not found* (module `MOM_energetic_PBL` inactive) |
| `MSTAR_CONV_ADJ` | `0.66` | *not found* (module `MOM_energetic_PBL` inactive) |
| `USE_MLD_ITERATION` | `True` | *not found* (module `MOM_energetic_PBL` inactive) |
| `EPBL_TRANSITION_SCALE` | `0.01` | *not found* (module `MOM_energetic_PBL` inactive) |
| `MLD_ITERATION_GUESS` | `False` | *not found* (module `MOM_energetic_PBL` inactive) |
| `EPBL_MLD_TOLERANCE` | `1.0` | *not found* (module `MOM_energetic_PBL` inactive) |
| `EPBL_MLD_BISECTION` | `True` | *not found* (module `MOM_energetic_PBL` inactive) |
| `EPBL_MLD_MAX_ITS` | `20` | *not found* (module `MOM_energetic_PBL` inactive) |
| `EPBL_MIN_MIX_LEN` | `0.0` | *not found* (module `MOM_energetic_PBL` inactive) |
| `MIX_LEN_EXPONENT` | `1.0` | *not found* (module `MOM_energetic_PBL` inactive) |
| `EPBL_VEL_SCALE_SCHEME` | `REICHL_H18` | *not found* (module `MOM_energetic_PBL` inactive) |
| `WSTAR_USTAR_COEF` | `15.0` | *not found* (module `MOM_energetic_PBL` inactive) |
| `EPBL_VEL_SCALE_FACTOR` | `0.5477` | *not found* (module `MOM_energetic_PBL` inactive) |
| `VSTAR_SURF_FAC` | `1.8258` | *not found* (module `MOM_energetic_PBL` inactive) |
| `USE_LA_LI2016` | `True` | *not found* (module `MOM_energetic_PBL` inactive) |
| `EPBL_LANGMUIR_SCHEME` | `ADDITIVE` | *not found* (module `MOM_energetic_PBL` inactive) |
| `LT_ENHANCE_COEF` | `0.1056` | *not found* (module `MOM_energetic_PBL` inactive) |
| `LT_ENHANCE_EXP` | `-1.0` | *not found* (module `MOM_energetic_PBL` inactive) |
| `LT_MOD_LAC1` | `0.0` | *not found* (module `MOM_energetic_PBL` inactive) |
| `LT_MOD_LAC2` | `0.0` | *not found* (module `MOM_energetic_PBL` inactive) |
| `LT_MOD_LAC3` | `0.0` | *not found* (module `MOM_energetic_PBL` inactive) |
| `LT_MOD_LAC4` | `0.8` | *not found* (module `MOM_energetic_PBL` inactive) |
| `LT_MOD_LAC5` | `0.8` | *not found* (module `MOM_energetic_PBL` inactive) |

### `MOM_regularize_layers`

| Parameter | GFDL | NCAR |
|---|---|---|
| `REGULARIZE_SURFACE_LAYERS` | `False` | <-------- |

### `MOM_opacity`

| Parameter | GFDL | NCAR |
|---|---|---|
| `OPACITY_SCHEME` | `MANIZZA_05` | *not found* (module `MOM_opacity` active — parameter not queried) |
| `BLUE_FRAC_SW` | `0.5` | *not found* (module `MOM_opacity` active — parameter not queried) |
| `EXP_OPACITY_SCHEME` | *not found* (module `MOM_opacity` active — parameter not queried) | `SINGLE_EXP` |
| `PEN_SW_SCALE` | *not found* (module `MOM_opacity` active — parameter not queried) | `0.0` |
| `PEN_SW_FRAC` | *not found* (module `MOM_opacity` active — parameter not queried) | `0.0` |
| `PEN_SW_NBANDS` | `3` | `1` |
| `OPTICS_2018_ANSWERS` | `False` | *not found* (module `MOM_opacity` active — parameter not queried) |
| `OPTICS_ANSWER_DATE` | `99991231` | <-------- |
| `PEN_SW_FLUX_ABSORB` | `2.5E-11` | <-------- |
| `PEN_SW_ABSORB_MINTHICK` | `1.0` | <-------- |
| `OPACITY_LAND_VALUE` | `10.0` | <-------- |

### `MOM_tracer_advect`

| Parameter | GFDL | NCAR |
|---|---|---|
| `TRACER_ADVECTION_SCHEME` | `PPM:H3` | <-------- |
| `USE_HUYNH_STENCIL_BUG` | *not found* (module `MOM_tracer_advect` active — parameter not queried) | `False` |

### `MOM_tracer_hor_diff`

| Parameter | GFDL | NCAR |
|---|---|---|
| `KHTR` | `0.0` | <-------- |
| `KHTR_MIN` | `0.0` | <-------- |
| `KHTR_MAX` | `0.0` | <-------- |
| `KHTR_PASSIVITY_COEFF` | `0.0` | <-------- |
| `KHTR_PASSIVITY_MIN` | `0.5` | <-------- |
| `DIFFUSE_ML_TO_INTERIOR` | `False` | <-------- |
| `CHECK_DIFFUSIVE_CFL` | `True` | <-------- |
| `MAX_TR_DIFFUSION_CFL` | `-1.0` | <-------- |
| `RECALC_NEUTRAL_SURF` | `False` | <-------- |

### `MOM_neutral_diffusion`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_NEUTRAL_DIFFUSION` | `False` | <-------- |

### `MOM_lateral_boundary_diffusion`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_LATERAL_BOUNDARY_DIFFUSION` | `False` | *not found* (module `MOM_lateral_boundary_diffusion` inactive) |

### `MOM_hor_bnd_diffusion`

| Parameter | GFDL | NCAR |
|---|---|---|
| `USE_HORIZONTAL_BOUNDARY_DIFFUSION` | *not found* (module `MOM_hor_bnd_diffusion` inactive) | `False` |
| `OBSOLETE_DIAGNOSTIC_IS_FATAL` | `True` | <-------- |

### `MOM_sum_output`

| Parameter | GFDL | NCAR |
|---|---|---|
| `CALCULATE_APE` | `False` | <-------- |
| `WRITE_STOCKS` | `True` | <-------- |
| `MAXTRUNC` | `1000` | `1000000` |
| `MAX_ENERGY` | `0.0` | <-------- |
| `MAXVEL` | `6.0` | <-------- |
| `ENERGYFILE` | `ocean.stats` | <-------- |
| `DATE_STAMPED_STDOUT` | `True` | <-------- |
| `ISO_DATE_STAMPED_STDOUT` | *not found* (module `MOM_sum_output` active — parameter not queried) | `False` |
| `TIMEUNIT` | `8.64E+04` | <-------- |
| `ENERGYSAVEDAYS` | `1.0` | <-------- |
| `ENERGYSAVEDAYS_GEOMETRIC` | `0.0` | <-------- |

### `ocean_stochastics_init`

| Parameter | GFDL | NCAR |
|---|---|---|
| `DO_SPPT` | `False` | <-------- |
| `DO_SKEB` | *not found* (module `ocean_stochastics_init` active — parameter not queried) | `False` |
| `PERT_EPBL` | `False` | <-------- |
| `STOCHASTICS_ANSWER_DATE` | *not found* (module `ocean_stochastics_init` active — parameter not queried) | `20250101` |

### `ocean_model_init`

| Parameter | GFDL | NCAR |
|---|---|---|
| `SINGLE_STEPPING_CALL` | `True` | <-------- |
| `RESTART_CONTROL` | `1` | `3` |
| `OCEAN_SURFACE_STAGGER` | `C` | <-------- |
| `EPS_OMESH` | *not found* (module `ocean_model_init` active — parameter not queried) | `1.0E-04` |
| `RESTORE_SALINITY` | `False` | <-------- |
| `RESTORE_TEMPERATURE` | `False` | <-------- |
| `ICE_SHELF` | `False` | <-------- |
| `ICEBERGS_APPLY_RIGID_BOUNDARY` | `False` | <-------- |
| `USE_WAVES` | `False` | <-------- |

### `MOM_surface_forcing`

| Parameter | GFDL | NCAR |
|---|---|---|
| `APPROX_NET_MASS_SRC` | `False` | *not found* (module `MOM_surface_forcing` inactive) |
| `SURFACE_FORCING_2018_ANSWERS` | `False` | *not found* (module `MOM_surface_forcing` inactive) |
| `SURFACE_FORCING_ANSWER_DATE` | `99991231` | *not found* (module `MOM_surface_forcing` inactive) |
| `FIX_USTAR_GUSTLESS_BUG` | `True` | *not found* (module `MOM_surface_forcing` inactive) |

### `MOM_surface_forcing_nuopc`

| Parameter | GFDL | NCAR |
|---|---|---|
| `LATENT_HEAT_FUSION` | `3.34E+05` | <-------- |
| `LATENT_HEAT_VAPORIZATION` | `2.5E+06` | <-------- |
| `MAX_P_SURF` | `0.0` | <-------- |
| `ADJUST_NET_SRESTORE_TO_ZERO` | `False` | <-------- |
| `ADJUST_NET_SRESTORE_BY_SCALING` | `False` | <-------- |
| `ADJUST_NET_FRESH_WATER_TO_ZERO` | `False` | `True` |
| `USE_NET_FW_ADJUSTMENT_SIGN_BUG` | *not found* (module `MOM_surface_forcing_nuopc` inactive) | `False` |
| `ADJUST_NET_FRESH_WATER_BY_SCALING` | `False` | <-------- |
| `ICE_SALT_CONCENTRATION` | `0.005` | <-------- |
| `USE_LIMITED_PATM_SSH` | `True` | <-------- |
| `WIND_STAGGER` | `C` | `A` |
| `WIND_STRESS_MULTIPLIER` | `1.0` | <-------- |
| `ENTHALPY_FROM_COUPLER` | *not found* (module `MOM_surface_forcing_nuopc` inactive) | `True` |
| `CD_TIDES` | `0.0018` | <-------- |
| `READ_TIDEAMP` | `False` | <-------- |
| `UTIDE` | `0.0` | <-------- |
| `READ_GUST_2D` | `False` | <-------- |
| `GUST_CONST` | `0.0` | `4.0E-04` |
| `USTAR_GUSTLESS_BUG` | *not found* (module `MOM_surface_forcing_nuopc` inactive) | `False` |
| `USE_RIGID_SEA_ICE` | `True` | <-------- |
| `SEA_ICE_MEAN_DENSITY` | `900.0` | <-------- |
| `SEA_ICE_VISCOSITY` | `1.0E+09` | <-------- |
| `SEA_ICE_RIGID_MASS` | `100.0` | <-------- |
| `ALLOW_ICEBERG_FLUX_DIAGNOSTICS` | `False` | <-------- |
| `ALLOW_GLC_RUNOFF_DIAGNOSTICS` | *not found* (module `MOM_surface_forcing_nuopc` inactive) | `False` |
| `ALLOW_FLUX_ADJUSTMENTS` | `False` | <-------- |
| `LIQUID_RUNOFF_FROM_DATA` | *not found* (module `MOM_surface_forcing_nuopc` inactive) | `False` |

### `MOM_file_parser`

| Parameter | GFDL | NCAR |
|---|---|---|
| `SEND_LOG_TO_STDOUT` | `False` | <-------- |
| `DOCUMENT_FILE` | `MOM_parameter_doc` | <-------- |
| `COMPLETE_DOCUMENTATION` | `True` | <-------- |
| `MINIMAL_DOCUMENTATION` | `True` | <-------- |
