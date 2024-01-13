README file for World Tremor Database folder
Link: http://www-solid.eps.s.u-tokyo.ac.jp/~idehara/wtd0/Welcome.html

Summary:
The World Tremor Database details various catalogs from around the world. 

The following regions can be found on the website:
- Nankai (Japan)
- Kyushu (Japan)
- Cascadia (Western US)
- Parkfield (Western US)
- Jalisco-Colima (Mexico)
- Guerrero MASE/GGAP (Mexico)
- Manawatu (New Zealand)
- Taiwan
- Southern Chile

CSV File Formats:
Each CSV file is titled as REGION-STARTDATE-ENDDATE.csv.
Dates are in YYYYMMDD format.

The datasets in the Google Drive folder have been downloaded WITHOUT clustering.
The website defines clustering as "two or more events within a space-time window"
with an "epicentral distance of 10 km and time difference of 1 hour."

The format of the raw CSV file is as follows:
1. Source origin date
2. Source origin time (Japan: JST=UTC+9, others UTC)
3. Latitude (deg)
4. Longitude (deg)
5. Depth (km)
6. Mw
7. Source duration [sec] (We adopt > 10 sec)
8. Residual error [sec] (We adopt < 1.5 sec)
9. Optional: Origin date & time with mili-seconds
