README file for Syria Historical Earthquakes

Citation for the paper:
Sbeinati, Mohamed Reda et al. “The historical earthquakes of Syria: an analysis of large and moderate earthquakes from 1365 B.C. to 1900 A.D.” Annals of Geophysics 48 (2009): n. pag.

Summary:
CSV file containing ancient Syrian earthquakes from 1365 B.C. to 1900 A.D.

The header of the CSV file has the following details:
- DateTime: (string) datetime object of the event
- Magnitude: (int) strength of the earthquake using the nomograph proposed by Shebalin (1970)--reference from the paper
- Latitude: (int) Latitude of the absolute location (degrees N)
- Longitude: (int) Longitude of the absolute location (degrees E)
- Depth: (int) in km, the distance from the epicenter to the focus of the earthquake

Cleaning Pipeline:

1. The data from the paper with the filename `The historical earthquakes of Syria.pdf`  is scraped with the following columns: Date, Lat, Long, Major affected localities, I0, H, Ms. The output filename is `SyriaHistoricalEarthquakes1.csv`.
2. Manual cleaning
    - For date intervals, choose one specific day from the interval (we chose one of the bounds).
    - For dates with no month or day, the default is 01-01 or January 1st.
    - Remove unnecessary strings.
3. Run `syria_cleaning.py`.The output filename will be `SyriaHistoricalEarthquakes2.csv`.
    - Manually convert the years at the top since the parser automatically treats it as an event in the 21st century, e.g. 2037->0037
