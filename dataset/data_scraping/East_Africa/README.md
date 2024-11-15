#####################################
#      DATABASE INFORMATION
#####################################
This is the southern East African Rift System (EARS) database described in Holmgren et al. (2023, Earthquake Spectra). It contains five flatfile spreadsheets, two frequency-vector files, and one time-series directory.

Five flatfile spreadsheets:
     1) SouthEARS_EarthquakeCatalog.csv   = earthquake catalog with the relocation results
     2) SouthEARS_EventPhasePicks.csv     = P and S wave arrival times in absolute time for each earthquake record within 300 km in the timeseries database
     3) SouthEARS_FASTable.csv            = Fourier amplitude spectrum flatfile
     4) SouthEARS_GroundMotionTable.csv   = ground-motion table with PGA, PGV, and 5% damped PSA
     5) SouthEARS_StationCatalog.csv      = station metadata

Two additional files with the PSA frequencies and FAS frequencies are provided:
     1) SouthEARS_PSA_Frequencies.csv     = matches the PSA column headers in SouthEARS_GroundMotionTable.csv to the frequency value
     2) SouthEARS_FAS_Frequencies.csv     = matches the FAS column headers in SouthEARS_FASTable.csv to the frequency value
    
One directory of 10,725 instrument-corrected SAC time-series. The time-series are organized into event folders with names following the format yyyymmdd_HHMMSS, matching the event name id in the earthquake catalog. The individual SAC files have names based on the seismic network, station name, and component, such as: MW_ZOMB_BHN.SAC. Any records for which instrument response was not available will have "_raw" appended to the file name, e.g., MW_ZOME_BHN_raw.SAC. The units are in m/s for the broadband, high-broadband, and geophone instruments (BH*, HH*, and HP*), and m/s^2 for the accelerometers (HN* or EN*). The XD temporary network is in nm/s (1e-9m/s).



#####################################
#      HEADER INFORMATION
#####################################
#________________________________________________________________________________________________
# SouthEARS_EarthquakeCatalog.csv

# Header info:
EventName = name of the event based on original catalog's origin time
Mw = moment magnitude, either from original catalog or converted using Poggi et al. (2017) Table 2
MwConvFlag = flag for converted Mw. 1 = converted, 0 = original Mw
orig_mag = original catalog's reported magnitude
orig_magType = original catalog's reported magnitude type
orig_magCat = agency which reported the original catalog's magnitude
orig_OriginTime = original catalog's origin time in IRIS format
orig_Lat_deg = original catalog's latitude in degrees
orig_Lon_deg = original catalog's longitude in degrees
orig_Depth_km = original catalog's depth in km

# Three velocity models were used in nonlinloc for each event: E19 (Ebinger et al., 2019), S21 (Stevens et al., 2021), and CRUST1 (CRUST1.0)
# For each velocity model used in nonlinloc, the following fields are given:    

XX_OriginTime = Origin time in IRIS format
XX_Lat_deg = Latitude in degrees
XX_Lon_deg = Longitude in degrees
XX_Depth_km = depth in km
XX_DepthErr_km = depth error estimated from the 68% confidence ellipsoid in km
XX_LocErr_km = semi-major axis length of the 68% confidence ellipsoid i nkm
XX_RMSTimeErr_sec = root-mean-square of the time error in seconds
XX_NumSta = number of stations used in relocation (number of phases = 2xNumSta)
XX_StaAzGap_deg = maximum azimuth gap between stations used for location in degrees

# If available, the style of faulting is provided as the strike, dip, and rake:
fm_strike_deg = focal mechanism strike in degrees
fm_dip_deg = focal mechanism dip in degrees
fm_rake_deg = focal mechanism rake in degrees
fmCat = catalog from which the focal mechanism was obtained. GCMT, ISC, NEIC, and PRE are from the ISC bulletin, Biggs2010 = Biggs et al. (2010, GRL),  and Ebinger2019 = Ebinger et al. (2019, Geochemistry, Geophysics, Geosystems)


#________________________________________________________________________________________________
# SouthEARS_EventPhasePicks.csv

# Header info:
EventName = name of the event based on original catalog's origin time (see SouthEARS_EarthquakeCatalog.csv)
net = network code
sta = station name
inst = instrument type (first two letters of the component name, e.g. BH* or EN*)
P = P-wave arrival time in absolute time (IRIS format)
S = S-wave arrival time in absolute time (IRIS format)
SPtime = difference in P- and S-wave arrival times (seconds)
stationTimingErrorFlag = 0 if fine, 1 if there is a station timing error larger than 10 seconds


#________________________________________________________________________________________________
# SouthEARS_FAS_Frequencies.csv

# Header info:
fnum = column header for frequency value found in SouthEARS_FASTable.csv, 212 frequencies in total
freq_Hz = corresponding frequency value in Hz


#________________________________________________________________________________________________
# SouthEARS_FASTable.csv

# Header info:
EventName = name of the event based on original catalog's origin time (see SouthEARS_EarthquakeCatalog.csv)
Mw = moment magnitude, either from original catalog or converted using Poggi et al. (2017) Table 2
MwConvFlag = flag for converted Mw. 1 = converted, 0 = original Mw
orig_mag = original catalog's reported magnitude
orig_magType = original catalog's reported magnitude type
net = network code
sta = station name
inst = instrument component code (first two letters, e.g. BH*)
VS30 = USGS global VS30 value (m/s) (Heath et al., 2020)

# Three velocity models were used in nonlinloc for each event: E19 (Ebinger et al., 2019), S21 (Stevens et al., 2021), and CRUST1 (CRUST1.0)
# For each velocity model used in nonlinloc, the following fields are given:    

XX_depth = depth in km
XX_repi = epicentral distance in km
XX_rhypo = hypocentral distance in km
XX_loc_ok = flag for acceptable locations based on SP time and rhypo, 1 = accepted location (see Equation 1, Holmgren et al., 2023)
XX_loc_nll = flag for if event has been relocated using nonlinloc, 1 = yes

freqLimitsMin = minimum frequency considered for the FAS
freqLimitsMax = maximum frequency considered fro the FAS
fas_type = E, N, or EAS (effective amplitude spectrum)
frequencies = 212 frequency steps between 0.1 to 30 Hz for the acceleration FAS (m/s), see SouthEARS_FAS_Frequencies.csv for column head frequency value


#________________________________________________________________________________________________
# SouthEARS_GroundMotionTable.csv

# Header info:
EventName = name of the event based on original catalog's origin time (see SouthEARS_EarthquakeCatalog.csv)
Mw = moment magnitude, either from original catalog or converted using Poggi et al. (2017) Table 2
MwConvFlag = flag for converted Mw. 1 = converted, 0 = original Mw
orig_mag = original catalog's reported magnitude
orig_magType = original catalog's reported magnitude type
net = network code
sta = station name
inst = instrument component code (first two letters, e.g. BH*)
VS30 = USGS global VS30 value (m/s) (Heath et al., 2020)

# Three velocity models were used in nonlinloc for each event: E19 (Ebinger et al., 2019), S21 (Stevens et al., 2021), and CRUST1 (CRUST1.0)
# For each velocity model used in nonlinloc, the following fields are given:    

XX_depth = depth in km
XX_repi = epicentral distance in km
XX_rhypo = hypocentral distance in km
XX_loc_ok = flag for acceptable locations based on SP time and rhypo, 1 = accepted location (see Equation 1, Holmgren et al., 2023)
XX_loc_nll = flag for if event has been relocated using nonlinloc, 1 = yes

freqLimitsMin = minimum frequency considered for the response spectra
freqLimitsMax = maximum frequency considered fro the response spectra
psa_type = E, N, or rotD50
PGA = peak ground acceleration (m/s^2)
PGV = peak ground velocity (m/s)
frequencies = 291 frequency steps between 1 to 30 Hz for the 5% damped pseudo-spectral acceleration (m/s^2), see SouthEARS_PSA_Frequencies.csv for column head frequency value


#________________________________________________________________________________________________
# SouthEARS_PSA_Frequencies.csv

# Header info:
fnum = column header for frequency value found in SouthEARS_GroundMotionTable.csv, 291 frequencies in total
freq_Hz = corresponding frequency value in Hz


#________________________________________________________________________________________________
# SouthEARS_StationCatalog.csv

# Header info:
net = network code
sta = station name
lat = latitude in degrees
lon = longitude in degrees
el = elevation in meters
inst = instrument types available, first two letter of component name (e.g. BH*, HH*)
VS30 = USGS VS30 (m/s) (Heath et al., 2020)
notes = additional notes about station timing error, amplitude, or instrument response issues.