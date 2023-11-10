# import helper functions for data merging
import sys
sys.path.append("src/merge")
from helper import round_row

import pandas as pd

# 1. Load all files to merge
csv_files = ["src/merge/asia/Asia-Combined.csv",
             "src/merge/misc/Misc-Combined.csv",
             "src/merge/noaa/NOAA-Combined.csv",
             "src/merge/north_america/North-America-Combined.csv",
             "src/merge/world_tremor/World-Tremor-Combined.csv",
             "src/merge/usgs_pre_1950/USGS1800-1949.csv"]

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

        # find the rounded time, mag, lat, and long values
        # find helper.py for details about this function
        rtime, rmag, rlat, rlon = round_row(row)

        # if we've never seen this key before, intialize a list
        # this represents all earthquakes at this time
        if rtime not in seen:
            seen[rtime] = []
        
        # if we've seen this earthquake before at this time, it's a duplicate!
        if (rmag, rlat, rlon) in seen[rtime]:
            continue
        
        # otherwise, treat this earthquake as unique
        # append the data into the result
        result.append([row["Timestamp"], row["Magnitude"], row["Latitude"], row["Longitude"], row["Depth"]])

# 4. Sort the earthquakes in increasing order
result.sort(key=lambda x: x[0])

# 5. Convert the result list to DataFrame and export it
# O(nlogn) time due to sorting
# O(n) extra space for newly-created lists
result_df = pd.DataFrame(result, columns=['Timestamp', 'Magnitude', 'Latitude', 'Longitude', 'Depth'])
result_df.to_csv("src/merge/various/Various-Combined.csv", index=False)
