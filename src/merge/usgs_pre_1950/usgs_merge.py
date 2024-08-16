# import helper functions for data merging
import sys
sys.path.append("src/merge")
from helper import round_row

import pandas as pd

# 1. Load all files to merge
csv_files = ["src/merge/usgs_pre_1950/input/USGS1800-1849.csv",
             "src/merge/usgs_pre_1950/input/USGS1850-1899.csv",
             "src/merge/usgs_pre_1950/input/USGS1900-1949.csv"]

# 2. Load the data frames
# The header will be ["Datetime", "Magnitude", "Longitude", "Latitude", "Depth"]
frames = [pd.read_csv(csv_file) for csv_file in csv_files]

# 3. Use a hashmap to keep track of duplicate earthquakes
# seen[time] = [magnitude, longitude, latitude]
seen = dict()
result = []

for frame in frames:
    for i in range(1, len(frame)):

        # access the current row
        row = frame.iloc[i]

        """
        Unique addition of code for USGS datasets:
        Localize timezones to remove UTC label
        """
        time = pd.Timestamp(row["Timestamp"])
        time = time.tz_localize(None).strftime('%Y-%m-%d %X')
        result.append([time, row["Magnitude"], row["Latitude"], row["Longitude"], row["Depth"]])

# 4. Sort the earthquakes in increasing order
result.sort(key=lambda x: x[0])

# 5. Convert the result list to DataFrame and export it
# O(nlogn) time due to sorting
# O(n) extra space for newly-created lists
result_df = pd.DataFrame(result, columns=['Timestamp', 'Magnitude', 'Latitude', 'Longitude', 'Depth'])
result_df.to_csv("src/merge/usgs_pre_1950/USGS1800-1949.csv", index=False)
