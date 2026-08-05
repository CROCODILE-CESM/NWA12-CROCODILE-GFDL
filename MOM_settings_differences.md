# Ocean configuration differences

This comparison covers the ocean component only, BGC/COBALT and sea-ice settings are excluded. 

The `MOM_*` files are compared. For NCAR, I compared the files from NWA12 run without river runoff. 

Values shown as `not set` are absent from that file, not necessarily explicitly disabled.

## Grid and domain

| Parameter | NWA12-GFDL | NWA12-NCAR | Source file(s) |
|---|---|---|---|
| `INPUTDIR` | `INPUT` | `/glade/campaign/cesm/cesmdata/inputdata/ocn/mom/ocean_hgrid` in `MOM_input`; `/glade/work/emilanese/croc_input/oleanderNWA12_2006-2026/ocnice` in `MOM_override` | `MOM_input (GFDL)`; `MOM_input (NCAR)`; `MOM_override (NCAR)` |
| `GRID_FILE` | `ocean_hgrid.nc` | `ocean_hgrid_ocean_hgrid_5a5356.nc` | `MOM_input (GFDL)`; `MOM_input (NCAR)`; `MOM_override (NCAR)` |
| `TOPO_FILE` | `ocean_topog.nc` | `ocean_topog_ocean_hgrid_5a5356.nc` | `MOM_input (GFDL)`; `MOM_input (NCAR)`; `MOM_override (NCAR)` |
| `NIGLOBAL` | 775 | 740 | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `NJGLOBAL` | 845 | 780 | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `NIHALO` | not set | 4 | `MOM_input (NCAR)` |
| `NJHALO` | not set | 4 | `MOM_input (NCAR)` |
| `REENTRANT_Y` | not set | `False` | `MOM_override (NCAR)` |
| `TRIPOLAR_N` | not set | `False` | `MOM_input (NCAR)` |
| `MAXIMUM_DEPTH` | 6500 | 8369.66015625 | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `MINIMUM_DEPTH` | 4 | 0 | `MOM_override (NCAR)` |
| `RAD_EARTH` | not set in `MOM_input` | 6371220 | `MOM_input (NCAR)` |

## Time stepping and vertical coordinates

| Parameter | NWA12-GFDL | NWA12-NCAR | Source file(s) |
|---|---|---|---|
| `DT` | 600 | 450 | `MOM_override (NCAR)` |
| `DT_THERM` | 1800 in `MOM_input`; 1200 in `MOM_parameter_doc.short` | 3600 in `MOM_input`, overridden to 1800 | `MOM_input (GFDL)`; `MOM_parameter_doc.short (GFDL)`; `MOM_input (NCAR)`; `MOM_override (NCAR)` |
| `DTBT_RESET_PERIOD` | not set | 0 | `MOM_input (NCAR)` |
| `NK` | 75 | 65 in `MOM_input`, overridden to 75 | `MOM_input (GFDL)`; `MOM_input (NCAR)`; `MOM_override (NCAR)` |
| `COORD_CONFIG` | `ALE` | `none` in `MOM_override` | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `ALE_COORDINATE_CONFIG` | `FILE:vgrid_75_2m.nc,dz` | `FILE:vgrid_65L_20200626.nc,dz` in `MOM_input`; `FILE:ocean_vgrid_ocean_hgrid_5a5356.nc` in `MOM_override` | `MOM_input (GFDL)`; `MOM_input (NCAR)`; `MOM_override (NCAR)` |
| `REGRIDDING_COORDINATE_MODE` | `Z*` | `Z*` | `MOM_input (GFDL)`; `MOM_parameter_doc.short (GFDL)` |
| `REMAPPING_SCHEME` | `PPM_H4` | `PPM_H4` | `MOM_parameter_doc.short (GFDL)` |
| `INIT_LAYERS_FROM_Z_FILE` | not set | `True` | `MOM_override (NCAR)` |
| `Z_INIT_ALE_REMAPPING` | not set | `True` | `MOM_input (NCAR)`; `MOM_override (NCAR)` |
| `Z_INIT_REMAP_OLD_ALG` | not set | `False` | `MOM_input (NCAR)` |
| `TEMP_SALT_INIT_VERTICAL_REMAP_ONLY` | not set | `True` | `MOM_override (NCAR)` |
| `MAX_LAYER_THICKNESS_CONFIG` | not set | `FNC1:400,31000.0,0.1,.01` | `MOM_input (NCAR)` |
| `MAXTRUNC` | 1000 | 1000000 | `MOM_input (GFDL)`; `MOM_parameter_doc.short (GFDL)`; `MOM_input (NCAR)` |

## Dynamics, mixing, and surface physics

| Parameter | NWA12-GFDL | NWA12-NCAR | Source file(s) |
|---|---|---|---|
| `LAPLACIAN` | `False` | `True` | `MOM_input (GFDL)`; `MOM_input (NCAR)` |
| `BIHARMONIC` | `True` | not set | `MOM_input (GFDL)` |
| `AH` | 0 | not set | `MOM_input (GFDL)` |
| `AH_VEL_SCALE` | 0.010 | 0.01 | `MOM_input (GFDL)`; `MOM_input (NCAR)` |
| `CDRAG` | 0.003 | not set | `MOM_input (GFDL)` |
| `DRAG_BG_VEL` | 0 | not set | `MOM_input (GFDL)` |
| `KVML` | 0 | not set | `MOM_input (GFDL)` |
| `KDML` | not set | 0 | `MOM_input (NCAR)` |
| `KH_VEL_SCALE` | not set | 0.01 | `MOM_input (NCAR)` |
| `HMIX_MIN` | not set | 2 | `MOM_input (NCAR)` |
| `USE_KPP` | not set/`False` in `MOM_parameter_doc.short` | `True` | `MOM_input (NCAR)` |
| `USE_LMD94` | not set/`False` in `MOM_parameter_doc.short` | `True` | `MOM_input (NCAR)` |
| `KPP_IS_ADDITIVE` | not set | `False` | `MOM_input (NCAR)` |
| `DOUBLE_DIFFUSION` | `True` | not set/`False` in `MOM_parameter_doc.short` | `MOM_input (GFDL)`; `MOM_parameter_doc.short (GFDL)` |
| `USE_CVMIX_DDIFF` | not set/`False` in `MOM_parameter_doc.short` | `True` | `MOM_input (NCAR)` |
| `USE_CVMix_CONVECTION` | not set/`False` in `MOM_parameter_doc.short` | `True` | `MOM_input (NCAR)` |
| `MIX_BOUNDARY_TRACER_ALE` | not set/`False` in `MOM_parameter_doc.short` | `True` | `MOM_input (NCAR)` |
| `PRANDTL_TURB` | 1.25 | not set | `MOM_parameter_doc.short (GFDL)` |
| `PRANDTL_BKGND` | not set/1 in `MOM_parameter_doc.short` | 10 | `MOM_input (NCAR)` |
| `N_SMOOTH` | not set | 3 | `MOM_input (NCAR)` |
| `N_SMOOTH_RI` | not set | 1 | `MOM_input (NCAR)` |
| `MATCH_TECHNIQUE` | not set | `MatchGradient` | `MOM_input (NCAR)` |
| `DO_RIVERMIX` | `True` | not set | `MOM_input (GFDL)` |
| `RIVERMIX_DEPTH` | 5 | not set | `MOM_input (GFDL)` |
| `DO_GEOTHERMAL` | `False` | `True` | `MOM_input (GFDL)`; `MOM_input (NCAR)` |
| `USE_PSURF_IN_EOS` | not set | `True` | `MOM_input (NCAR)` |
| `EQN_OF_STATE` | `WRIGHT` in `MOM_parameter_doc.short` | `WRIGHT_FULL` | `MOM_input (NCAR)` |
| `BOUND_CORIOLIS` | not set/`False` in `MOM_parameter_doc.short` | `True` | `MOM_input (NCAR)` |
| `GUST_CONST` | not set/0 in `MOM_parameter_doc.short` | 0.0004 | `MOM_input (NCAR)` |
| `CHECK_BAD_SURFACE_VALS` | not set/`False` in `MOM_parameter_doc.short` | `True` | `MOM_input (NCAR)` |
| `BAD_VAL_SSH_MAX` | not set | 50 | `MOM_input (NCAR)` |
| `BAD_VAL_SST_MAX` | not set | 65 | `MOM_input (NCAR)` |
| `BAD_VAL_SST_MIN` | not set | -3 | `MOM_input (NCAR)` |
| `USE_LAND_MASK_FOR_HVISC` | not set | `True` | `MOM_input (NCAR)` |
| `WIND_STAGGER` | not set/`C` in `MOM_parameter_doc.short` | `A` | `MOM_input (NCAR)` |

## Initial conditions and restart behavior

| Parameter | NWA12-GFDL | NWA12-NCAR | Source file(s) |
|---|---|---|---|
| `TS_CONFIG` | `file` | not set in `MOM_input`; replaced by `TEMP_SALT_Z_INIT_FILE` | `MOM_input (GFDL)`; `MOM_input (NCAR)` |
| `TS_FILE` | `glorys_ic_1993-01-01.nc` | not set | `MOM_input (GFDL)` |
| `TEMP_IC_VAR` | `temp` | not set | `MOM_input (GFDL)` |
| `SALT_IC_VAR` | `salt` | not set | `MOM_input (GFDL)` |
| `VELOCITY_CONFIG` | `file` | `file` | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `VELOCITY_FILE` | `glorys_ic_1993-01-01.nc` | `init_vel.nc` | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `SURFACE_HEIGHT_IC_FILE` | `glorys_ic_1993-01-01.nc` | `init_eta.nc` | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `SURFACE_HEIGHT_IC_VAR` | `ssh` | `eta_t` | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `TEMP_SALT_Z_INIT_FILE` | not set | `init_tracers.nc` | `MOM_override (NCAR)` |
| `Z_INIT_FILE_PTEMP_VAR` | not set | `temp` | `MOM_override (NCAR)` |
| `Z_INIT_FILE_SALT_VAR` | not set | `salt` | `MOM_override (NCAR)` |
| `U_IC_VAR` | not set | `u` | `MOM_override (NCAR)` |
| `V_IC_VAR` | not set | `v` | `MOM_override (NCAR)` |
| `SAVE_INITIAL_CONDS` | `False` | `True` | `MOM_input (GFDL)`; `MOM_input (NCAR)` |
| `PARALLEL_RESTARTFILES` | `False` | `True` | `MOM_parameter_doc.all (GFDL)`; `MOM_input (NCAR)` |
| `RESTART_CONTROL` | 1 in `MOM_parameter_doc.all` | 3 | `MOM_input (NCAR)` |
| `RESTART_CHECKSUMS_REQUIRED` | `True` in `MOM_parameter_doc.all` | `False` | `MOM_input (NCAR)` |
| `IC_OUTPUT_FILE` | `MOM_IC` in `MOM_parameter_doc.short` | `oleanderNWA12_2006-2026.mom6.ic.2006-01-01.nc` | `MOM_parameter_doc.short (GFDL)`; `MOM_input (NCAR)` |

## Open boundaries

| Parameter | NWA12-GFDL | NWA12-NCAR | Source file(s) |
|---|---|---|---|
| `OBC_NUMBER_OF_SEGMENTS` | 3 | 4 | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `OBC_SEGMENT_001` | `J=0,I=0:N,...` | `J=N,I=N:0,...` | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `OBC_SEGMENT_002` | `J=N,I=N:0,...` | `J=0,I=0:N,...` | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `OBC_SEGMENT_003` | `I=N,J=0:N,...` | same geometry | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `OBC_SEGMENT_004` | not set | `I=0,J=N:0,...` | `MOM_override (NCAR)` |
| `OBC_SEGMENT_001_DATA` | `uv_001.nc`, `zos`, `thetao`, `so`, tidal fields | `forcing_obc_segment_001.nc`, `eta`, `temp`, `salt` | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `OBC_SEGMENT_002_DATA` | `uv_002.nc`, `zos`, `thetao`, `so`, tidal fields | `forcing_obc_segment_002.nc`, `eta`, `temp`, `salt` | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `OBC_SEGMENT_003_DATA` | `uv_003.nc`, `zos`, `thetao`, `so`, tidal fields | `forcing_obc_segment_003.nc`, `eta`, `temp`, `salt` | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `OBC_SEGMENT_004_DATA` | not set | `forcing_obc_segment_004.nc`, `eta`, `temp`, `salt` | `MOM_override (NCAR)` |
| `OBC_SEGMENT_001_VELOCITY_NUDGING_TIMESCALES` | `3.0,360.0` | `0.3,360.0` | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `OBC_SEGMENT_002_VELOCITY_NUDGING_TIMESCALES` | `3.0,360.0` | `0.3,360.0` | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `OBC_SEGMENT_003_VELOCITY_NUDGING_TIMESCALES` | `3.0,360.0` | `0.3,360.0` | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `OBC_SEGMENT_004_VELOCITY_NUDGING_TIMESCALES` | not set | `0.3,360.0` | `MOM_override (NCAR)` |
| `OBC_TRACER_RESERVOIR_LENGTH_SCALE_IN` | 9000 | 3000 | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `OBC_TRACER_RESERVOIR_LENGTH_SCALE_OUT` | 9000 | 30000 | `MOM_input (GFDL)`; `MOM_override (NCAR)` |
| `BRUSHCUTTER_MODE` | not set | `True` | `MOM_override (NCAR)` |
| `RAMP_OBCS` | `False` | not set | `MOM_input (GFDL)` |

## Tides

| Parameter | NWA12-GFDL | NWA12-NCAR | Source file(s) |
|---|---|---|---|
| `TIDES` | `True` | not set/`False` in `MOM_parameter_doc.all` | `MOM_input (GFDL)`; `MOM_parameter_doc.all (NCAR)` |
| `TIDE_M2`, `TIDE_S2`, `TIDE_N2`, `TIDE_K2` | `True` | not set | `MOM_input (GFDL)` |
| `TIDE_K1`, `TIDE_O1`, `TIDE_P1`, `TIDE_Q1` | `True` | not set | `MOM_input (GFDL)` |
| `TIDE_MM`, `TIDE_MF` | `True` | not set | `MOM_input (GFDL)` |
| `TIDE_REF_DATE` | `1993,1,1` | not set | `MOM_input (GFDL)` |
| `TIDE_SAL_SCALAR_VALUE` | 0.010 | not set | `MOM_input (GFDL)` |
| `TIDE_USE_EQ_PHASE` | `True` | not set | `MOM_input (GFDL)` |
| `OBC_TIDE_CONSTITUENTS` | `M2,S2,N2,K2,K1,O1,P1,Q1,MM,MF` | not set | `MOM_input (GFDL)`; `MOM_parameter_doc.short (GFDL)` |
| `OBC_TIDE_N_CONSTITUENTS` | 10 | 0 in `MOM_parameter_doc.all` | `MOM_input (GFDL)`; `MOM_parameter_doc.all (NCAR)` |

## Ocean diagnostics and geometry

| Parameter | NWA12-GFDL | NWA12-NCAR | Source file(s) |
|---|---|---|---|
| `NUM_DIAG_COORDS` | 1 | 2 | `MOM_parameter_doc.short (GFDL)`; `MOM_override (NCAR)` |
| `DIAG_COORDS` | `z Z ZSTAR` | `z Z ZSTAR,ole ZB ZSTAR` | `MOM_parameter_doc.short (GFDL)`; `MOM_override (NCAR)` |
| `DIAG_COORD_DEF_Z` | `FILE:diag_dz.nc,dz` | not set | `MOM_parameter_doc.short (GFDL)` |
| `DIAG_COORD_DEF_ZA` | not set | `UNIFORM` | `MOM_override (NCAR)` |
| `DIAG_COORD_DEF_ZB` | not set | `UNIFORM:100,1000.` | `MOM_override (NCAR)` |
| `GEOM_FILE` | not set | `oleanderNWA12_2006-2026.mom6.h.ocean_geometry.nc` | `MOM_input (NCAR)` |
| `WRITE_GEOM` | 0 | 1 in `MOM_parameter_doc.short` | `MOM_input (GFDL)`; `MOM_parameter_doc.short (NCAR)` |

## Ocean-only settings absent from the NWA12-NCAR files

| NWA12-GFDL setting absent from NWA12-NCAR | NWA12-GFDL value |
|---|---:|
| `AGGREGATE_FW_FORCING` | `True` |
| `BAROTROPIC_TIDAL_SAL_BUG` | `False` |
| `CORIOLIS_SCHEME` | `SADOURNY75_ENERGY` |
| `ETA_TOLERANCE_AUX` | 0.001 |
| `FOX_KEMPER_ML_RESTRAT_COEF2` | 0 |
| `IGNORE_FLUXES_OVER_LAND` | `True` |
| `INT_TIDE_DECAY_SCALE` | 300 |
| `INT_TIDE_DISSIPATION` | `False` |
| `INT_TIDE_PROFILE` | `POLZIN_09` |
| `LA_DEPTH_RATIO` | 0.2 |
| `LT_ENHANCE_COEF` | 0.1056 |
| `LT_ENHANCE_EXP` | -1 |
| `LT_MOD_LAC1` | 0 |
| `LT_MOD_LAC4` | 0.8 |
| `LT_MOD_LAC5` | 0.8 |
| `MASKING_DEPTH` | 1 |
| `MAX_RINO_IT` | 25 |
| `MIX_LEN_EXPONENT` | 1 |
| `ML_OMEGA_FRAC` | 0.001 |
| `MSTAR_CAP` | 10 |
| `MSTAR_CONV_ADJ` | 0.66 |
| `NSTAR` | 0.06 |
| `OPTICS_2018_ANSWERS` | `False` |
| `PEN_SW_FRAC` | 0.42 |
| `PEN_SW_NBANDS` | 3 |
| `PEN_SW_SCALE` | 10 |
| `RH18_MSTAR_CN3` | -6 |
| `SPONGE` | `False` |
| `SPONGE_UV` | `False` |
| `TKE_DECAY` | 0.001 |
| `USE_JACKSON_PARAM` | `True` |
| `USE_LA_LI2016` | `True` |
| `VAR_PEN_SW` | `True` |
| `VSTAR_SURF_FAC` | 1.8258 |
| `WSTAR_USTAR_COEF` | 15 |
