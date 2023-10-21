import pandas as pd

#This code is for when you are checking for duplicate earthquakes

# 1. Load the non-Japan files from the World Tremor Database
# Japan datasets are in JST=UTC+9, instead of UTC; needs to be converted later
csv_files = ["src/merge/global/input/Southern-Chile.20050101-20070228.csv",
            #  "src/merge/global/input/Kyushu-20040401-20130331.csv",
            #  "src/merge/global/input/Nankai-20040401-20130329.csv",
             "src/merge/global/input/Guerrero-GGAP-20091126-20130817.csv",
             "src/merge/global/input/Guerrero-MASE-20050101-20070606.csv",
             "src/merge/global/input/Jalisco-Colima-20060126-20070609.csv",
             "src/merge/global/input/Manawatu-20040501-20120430.csv",
             "src/merge/global/input/Taiwan.20060101-20091231.csv",
             "src/merge/global/input/Cascadia-20050101-20141231.csv",
             "src/merge/global/input/Parkfield-20100101-20121231.csv"]

# 2. Load the data frames
# World Tremor Datasets don't have headers, so let's add some
frames = [pd.read_csv(csv_file,
                      names=["date", "time", "latitude", "longitude", "depth",
                             "mw", "duration", "error", "optional"])
            for csv_file in csv_files]

# 3. Use a hashmap to keep track of duplicate earthquakes
# seen[time] = [magnitude, longitude, latitude]
seen = dict()
result = []

for frame in frames:
    for i in range(len(frame)):

        # access the current row
        row = frame.iloc[i]

        # find the time and date
        date = row["date"].split("-")
        year, month, day = [int(d) for d in date]

        time = row["time"].split(":")
        hour, minute, second = [int(t) for t in time]

        # convert the data into a pd.Timestamp object
        frame_time = pd.Timestamp(year=year, month=month, day=day,
                                  hour=hour, minute=minute, second=second)
        
        # append the data into the result
        result.append([frame_time, row["mw"], row["longitude"], row["latitude"], row["depth"]])

# 4. Sort the earthquakes in increasing order
result.sort(key=lambda x: x[0])

# 5. Convert the result list to DataFrame and export it
# O(nlogn) time due to sorting
# O(n) extra space for newly-created lists
result_df = pd.DataFrame(result, columns=['DateTime', 'Mw', 'Longitude', 'Latitude', 'Depth'])
result_df.to_csv("src/merge/global/World_Tremor.csv", index=False)
