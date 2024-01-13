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
            for i in range(3): next(input_file, None)

            # write each row from the txt file to the csv
            for line in input_file:
                row = line.split()

                try:
                    
                    # convert the date and time into a pd.Timestamp
                    datetime = f"{row[0]} {row[1]}"
                    ts = pd.Timestamp(datetime)
                    
                    # extract time information from the timestamp
                    year = ts.year
                    month = ts.month
                    day = ts.day
                    hour = ts.hour
                    minute = ts.minute
                    second = ts.second
                    millisecond = ts.microsecond // 1000
                    
                    # find the geographic information
                    magnitude = row[4]
                    latitude = row[6]
                    longitude = row[7]
                    depth = row[8]
                    
                    # write the information into the output csv
                    output_row = [year, month, day, hour, minute, second, millisecond,
                                  magnitude, latitude, longitude, depth]
                    csv_writer.writerow(output_row)
                
                except Exception as e:
                    print(str(e))


# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/SoCal/raw/SearchResults.txt"
    
    output_filename = "SCEDC (1932-2023)"
    output_path = f"src/scraper/SoCal/clean/{output_filename}.csv"
    
    find_quakes(input_path, output_path)
    clean_data(output_path)