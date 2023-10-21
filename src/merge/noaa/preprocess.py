import pandas as pd

def replace_with_datetime(input_df):
    output_df = []
    for i in range(1, len(input_df)):
        row = input_df.iloc[i]

        # find the time and date
        year = row["Year"]
        month = row["Month"]
        day = row["Day"]
        hour = row["Hour"]
        minute = row["Minute"]
        second = row["Second"]
        
        # create a timestamp sing these values
        frame_time = pd.Timestamp(year=year, month=month, day=day,
                                  hour=hour, minute=minute, second=second)
        
        # append the result into the table
        output_df.append([frame_time, row["Magnitude"], row["Longitude"], row["Latitude"], row["Depth"]])

    # convert the list into a dataframe then return the result
    output_df = pd.DataFrame(output_df, columns=['DateTime', 'Magnitude', 'Longitude', 'Latitude', 'Depth'])
    return output_df


def process_GHEA():
    csv_file = "src/merge/noaa/raw/GHEA.csv";
    input_df = pd.read_csv(csv_file)
    input_df = input_df[["Year", "Mo", "Da", "Ho", "Mi", "Se", "M", "Lon", "Lat", "Dep"]]
    input_df.rename(columns={"Year": "Year", "Mo": "Month", "Da": "Day", "Ho": "Hour",
                    "Mi": "Minute", "Se": "Second", "M": "Magnitude", "Lon": "Longitude",
                    "Lat": "Latitude", "Dep": "Depth"}, inplace=True)
    input_df.drop_duplicates()
    output_df = replace_with_datetime(input_df)
    output_df.to_csv("src/merge/noaa/input/GHEA.csv", index=False)

def process_NCEI():
    csv_file = "src/merge/noaa/raw/NCEI.csv";
    input_df = pd.read_csv(csv_file)
    input_df = input_df[["Year", "Mo", "Dy", "Hr", "Mn", "Sec", "Mag", "Longitude", "Latitude", "Focal Depth (km)"]]
    input_df.rename(columns={"Mo": "Month", "Dy": "Day", "Hr": "Hour",
                    "Mn": "Minute", "Sec": "Second", "Mag": "Magnitude",
                    "Focal Depth (km)": "Depth"}, inplace=True)
    input_df.drop_duplicates()
    output_df = replace_with_datetime(input_df)
    output_df.to_csv("src/merge/noaa/input/NCEI.csv", index=False)


def process_NOAA():
    csv_file = "src/merge/noaa/raw/NOAA.csv";
    input_df = pd.read_csv(csv_file)
    input_df = input_df[["YEAR", "MONTH", "DAY", "HOUR", "MINUTE", "SECOND", "MAGNITUDE", "LONGITUDE", "LATITUDE", "EQ_DEPTH"]]
    input_df.rename(columns={"YEAR": "Year", "MONTH": "Month", "DAY": "Day", "HOUR": "Hour",
                    "MINUTE": "Minute", "SECOND": "Second", "MAGNITUDE": "Magnitude",
                    "LONGITUDE": "Longitude", "LATITUDE": "Latitude", "EQ_DEPTH": "Depth"}, inplace=True)
    input_df.drop_duplicates()
    output_df = replace_with_datetime(input_df)
    output_df.to_csv("src/merge/noaa/input/NOAA.csv", index=False)

# rune the pre-processing functions
process_GHEA()
# process_NCEI()
# process_NOAA()