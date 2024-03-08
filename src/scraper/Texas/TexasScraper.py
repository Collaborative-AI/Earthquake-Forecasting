# import helper functions for data cleaning
import sys
sys.path.append("src/scraper")
from helper import clean_data

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
                row = line.split(",")

                try:
                    
                    # convert the date and time into a pd.Timestamp
                    datetime = f"{row[2]} {row[3]}"
                    ts = pd.Timestamp(datetime)
                    
                    # extract time information from the timestamp
                    year = ts.year
                    month = ts.month
                    day = ts.day
                    hour = ts.hour
                    minute = ts.minute
                    second = ts.second
                    millisecond = ts.microsecond // 1000

                    # find the other rows with data
                    # specifically record moment magnitude
                    magnitude = row[5]
                    latitude = row[6]
                    longitude = row[8]
                    
                    # note: MSL = mean sea level
                    # there are depth values relative to ground surface and MSL,
                    # and here, we choose MSL for consistency with other datasets
                    depth = row[10]

                    # reformat the line
                    output_row = [year, month, day, hour, minute, second, millisecond,
                                  magnitude, latitude, longitude, depth]
                    csv_writer.writerow(output_row)
                
                except Exception as e:
                    print(str(e))


# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/Texas/raw/texnet_events.csv"
    
    output_filename = "Texas (2016-2023)"
    output_path = f"src/scraper/Texas/clean/{output_filename}.csv"
    
    find_quakes(input_path, output_path)
    clean_data(output_path)