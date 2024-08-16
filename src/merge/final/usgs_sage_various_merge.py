import pandas as pd
import random
#This code is for when you are checking for duplicate earthquakes

# set a random seed for reproducibility
random.seed(2023)

"""
Modify the relative path to access your data. It can differ on your machine.
"""
RELATIVE_PATH = "src/merge/final/"

# 1. Load the USGS/SAGE merge
usgs_sage = pd.read_csv(RELATIVE_PATH + "USGS_SAGE_MERGED.csv")

# 2. Load all the remaining earthquakes in the dataset
various_combined = pd.read_csv(RELATIVE_PATH + "Various-Catalogs.csv")

# 2. Use a two-pointer approach
i, j = 0, 0
result = []

while i < len(usgs_sage) and j < len(various_combined):
    us_time = pd.Timestamp(usgs_sage.iloc[i]['DateTime']).tz_localize(None)
    vc_time = pd.Timestamp(various_combined.iloc[j]['Timestamp'])

    if abs((us_time - vc_time).total_seconds()) <= 10:
        if (abs(usgs_sage.iloc[i]['Latitude'] - various_combined.iloc[j]['Latitude']) <= 0.1 and
            abs(usgs_sage.iloc[i]['Longitude'] - various_combined.iloc[j]['Longitude']) <= 0.1 and
            abs(usgs_sage.iloc[i]['Magnitude'] - various_combined.iloc[j]['Magnitude']) <= 0.2):
            
            # Consider as the same earthquake, choose randomly
            if random.choice([True, False]):
                result.append([us_time,
                               usgs_sage.iloc[i]['Magnitude'],
                               usgs_sage.iloc[i]['Latitude'],
                               usgs_sage.iloc[i]['Longitude'],
                               usgs_sage.iloc[i]['Depth']])
            else:
                result.append([vc_time,
                               various_combined.iloc[j]['Magnitude'],
                               various_combined.iloc[j]['Latitude'],
                               various_combined.iloc[j]['Longitude'],
                               various_combined.iloc[j]['Depth']])
            
            i += 1
            j += 1
            continue
        
    elif us_time < vc_time:
        result.append([us_time,
                       usgs_sage.iloc[i]['Magnitude'],
                       usgs_sage.iloc[i]['Latitude'],
                       usgs_sage.iloc[i]['Longitude'],
                       usgs_sage.iloc[i]['Depth']])
        i += 1
        
    else:
        result.append([vc_time,
                       various_combined.iloc[j]['Magnitude'],
                       various_combined.iloc[j]['Latitude'],
                       various_combined.iloc[j]['Longitude'],
                       various_combined.iloc[j]['Depth']])
        j += 1

# 4. Convert the result list to DataFrame and export it
result_df = pd.DataFrame(result, columns=['DateTime', 'Magnitude', 'Latitude', 'Longitude', 'Depth'])
result_df.to_csv("src/merge/final/Completed-Merge.csv", index=False)
