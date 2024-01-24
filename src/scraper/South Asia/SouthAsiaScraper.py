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
                    
                    # find the time information from the csv
                    year = row[0]
                    month = row[1]
                    day = row[2]
                    hour = row[3]
                    minute = row[4]
                    second = row[5]
                    
                    # although milliseconds aren't present in this csv, 
                    # set the variable to 0 for consistency with other datasets
                    millisecond = 0

                    # find the other rows with data
                    magnitude = row[9]
                    latitude = row[6]
                    longitude = row[7]
                    depth = row[8]

                    # reformat the line
                    output_row = [year, month, day, hour, minute, second, millisecond,
                                  magnitude, latitude, longitude, depth]
                    csv_writer.writerow(output_row)
                
                except Exception as e:
                    print(str(e))


# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/South Asia/raw/11069_2016_2665_MOESM2_ESM.csv"
    
    output_filename = "South Asia (1900-2014)"
    output_path = f"src/scraper/South Asia/clean/{output_filename}.csv"
    
    find_quakes(input_path, output_path)
    clean_data(output_path)