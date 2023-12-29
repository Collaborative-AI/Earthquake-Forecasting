# **Fake Data Generation**

## A documentation for the fake data generated for the SmartQuake project.

### Files:

- FakeDataGenerator.py
  - This Python file creates a CSV with "fake" data to allow our machine learning model to differentiate between "real" and "fake" earthquakes.

### Sources:

We discovered the maximum longitude, latitude, and depth measurements for earthquakes in the following sources. The highlighted samples are also listed to 

- Maximum Longitude and Latitude:
  - https://www.google.com/search?client=firefox-b-1-d&q=maximum+longitude+and+latitude
  - "Latitude ranges between -90 and 90 degrees, inclusive. Values above or below this range will be clamped to the range [-90, 90]"
  - "Longitude ranges between -180 and 180 degrees, inclusive."
  - For our project, we will also use [-90, 90] for latitude and [-180, 180] for longitude instead of using cardinal symbols (i.e., N/S/W/E)

- Maximum Earthquake Depth:
  - https://www.usgs.gov/faqs/what-depth-do-earthquakes-occur-what-significance-depth
  - "Earthquakes occur in the crust or upper mantle, which ranges from the earth's surface to about 800 kilometers deep (about 500 miles)."
