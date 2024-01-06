README file for Wikipedia Historical Earthquakes

Source Link:
https://en.wikipedia.org/wiki/List_of_historical_earthquakes

Summary:
CSV file containing earthquakes from 1920 BCE to 1900 worldwide

The header of the CSV file has the following details:
- DateTime: (string) Date of the event
- Magnitude: (int) strength of the earthquake
- Latitude: (int) Latitude of the absolute location
- Longitude: (int) Longitude of the absolute location
- Depth: (int) in km, the distance from the epicenter to the focus of the earthquake

Cleaning Pipeline:
1. The data from Wikipedia was scraped with the following columns: DateTime, Magnitude, Latitude, Longitude. The output file is named `WikipediaEarthquakes1.csv.`
2. Add the depth column from the same site using `wiki_cleaning1.py`. The output file is named `WikipediaEarthquakes2.csv`
3. Manually clean the output file, `WikipediaEarthquakes2.csv.`
    1. Convert the intervals to the midpoint, i.e. 7-8 became 7.5.
    2. Remove the unnecessary strings.
4. Run `wiki_cleaning2.py`. Check for rows with “Invalid Date”. Manually, convert the dates since the script doesn’t cover all corner cases. Note: We manually converted some of the dates at the top. The output file will be named `WikipediaEarthquakes3.csv`.
