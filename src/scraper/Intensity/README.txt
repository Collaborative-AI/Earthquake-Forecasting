README file for U.S. Earthquake Intensity Database, 1638 to 1985

Summary:
XLSX file downloaded from NOAA database at https://ngdc.noaa.gov/hazard/eq-intensity.shtml
It was converted to a CSV file using Microsoft Excel. Some rows have missing data, such as
date/time and magnitude.

The website doesn't specify whether all earthquakes are recorded in UTC. However, considering
the LOCAL_TO_UTC column providing time zone offsets in relation to UTC, we'll correct time
zones to adjust to UTC.