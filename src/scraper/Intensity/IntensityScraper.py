# import helper functions for data cleaning
import sys
sys.path.append("src/scraper")
from helper import clean_data, sort_by_timestamp

# run on python 3.11.2
from csv import writer
import pandas as pd

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(input_path: str, output_path: str):
    
    with open(input_path, "r") as input_file:
        with open(output_path, "w") as out_file:

            # label the header of the csv with the appropriate labels
            csv_writer = writer(out_file, lineterminator="\n")
            header = ["Year", "Month", "Day", "Hour", "Minute", "Second", "Millisecond",
                      "Magnitude", "Latitude", "Longitude", "Depth"]
            csv_writer.writerow(header)
            next(input_file, None)

            # write each row from the txt file to the csv
            for line in input_file:
                
                try:
                    row = line.split(",")
                    
                    # find the time data
                    local_year = int(row[0])
                    local_month = int(row[1]) if row[1] else 1
                    local_day = int(row[2]) if row[2] else 1
                    local_hour = int(row[3]) if row[3] else 0
                    local_minute = int(row[4]) if row[4] else 0
                    
                    # seconds are formatted poorly in the input csv
                    local_second = local_millisecond = 0
                    
                    # if row[5] is a float (e.g., 44.6), then extract
                    # the second and millisecond value
                    if "." in row[5]:
                        total_milliseconds = int(float(row[5]) * 1000)
                        local_second, local_millisecond = divmod(total_milliseconds, 1000)
                    
                    # if row[5] is an int, then extract only the second
                    # if row[5] is neither an int or a float, do nothing
                    elif row[5]:
                        local_second = int(row[5])
                    
                    # find the timezone offset (LOCAL_TO_UTC)
                    tz_offset = -1 * int(row[6]) if row[6] else 0
                    
                    # the earthquakes in this dataset feature local times
                    # so we'll update the values to UTC
                    ts = pd.Timestamp(year=local_year, month=local_month, day=local_day,
                                    hour=local_hour, minute=local_minute, second=local_second,
                                    microsecond = local_millisecond*1000, tz=tz_offset)
                    ts = ts.tz_convert(tz="UTC")
                    
                    # find the updated time values
                    year = ts.year
                    month = ts.month
                    day = ts.day
                    hour = ts.hour
                    minute = ts.minute
                    second = ts.second
                    millisecond = ts.microsecond // 1000
                    
                    # find other earthquake attribute data
                    magnitude = row[10]
                    latitude = row[8]
                    longitude = row[9]
                    depth = row[11]
                    
                    # add the output row to the csv
                    output_row = [year, month, day, hour, minute, second, millisecond,
                                    magnitude, latitude, longitude, depth]
                    csv_writer.writerow(output_row)
                    
                except Exception as e:
                    print(str(e))
                    break

    
# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/Intensity/raw/eqint_tsqp.csv"
    
    output_filename = "U.S. Earthquake Intensity Database (1638-1985)"
    output_path = f"src/scraper/Intensity/clean/{output_filename}.csv"
    
    find_quakes(input_path, output_path)
    clean_data(output_path, sort=True)
