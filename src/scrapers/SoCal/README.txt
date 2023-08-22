README file for Southern California Earthquake Database Center (SCEDC)

Summary:
SoCalWebScraper.py web scrapes earthquakes from the SCEDC using the given
parameters set at https://service.scedc.caltech.edu/eq-catalogs/date_mag_loc.php

SoCalFileScraper.py scrapes a pre-downloaded TXT file from the SCEDC dataset
and converts it into a CSV file.

The following parameters were used for downloading the data in this folder:
Date formats are in YYYY/MM/DD, Hour:Minute:Second

Start Date:          1932/01/01, 00:00:00
End Date:            2023/07/25, 00:00:00
Min Magnitude:       1.0
Max Magnitude:       9.9
Min Depth (km):      0.0
Max Depth (km):      1000
Southern Lat:        30.0
Northern Lat:        39.0
West Longitude:      -124.0
East Longitude:      -111.0
Event Type:          Earthquake
Geographic Type:     Local
Use Legacy:          No

The following lines can be modified in SoCalWebScraper.py:
Line 35:        Modify the URL to web scrape data from
Line 36:        Modify the file path of the output .csv file

The following lines can be modified in SoCalFileScraper.py:
Line 25:        Modify the file path of the input .txt file
Line 26:        Modify the file path of the output .csv file