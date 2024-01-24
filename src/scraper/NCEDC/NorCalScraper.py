# import helper functions for data cleaning
import sys
sys.path.append("src/scraper")
from helper import clean_data

# run on python 3.11.2
from csv import writer
import pandas as pd

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(input_paths, output_path: str):
    
    with open(output_path, "w") as out_file:

        # label the header of the csv with the appropriate labels
        csv_writer = writer(out_file, lineterminator="\n")
        header = ["Year", "Month", "Day", "Hour", "Minute", "Second", "Millisecond",
                      "Magnitude", "Latitude", "Longitude", "Depth"]
        csv_writer.writerow(header)
    
        # store all input data into one output file
        for input_path in input_paths:
            with open(input_path, "r") as input_file:

                # skip the header of the input file
                next(input_file, None)

                # write each row from the txt file to the csv
                for line in input_file:
                    row = line.split(",")
                    
                    # convert the datetime into a pd.Timestamp object
                    ts = pd.Timestamp(row[0])
                    
                    # extract the attributes from the pd.Timestamp object
                    year = ts.year
                    month = ts.month
                    day = ts.day
                    hour = ts.hour
                    minute = ts.minute
                    second = ts.second
                    millisecond = ts.microsecond // 1000

                    # find the remaining columns
                    magnitude = row[4]
                    latitude = row[1]
                    longitude = row[2]
                    depth = row[3]

                    # reformat the line
                    output_row = [year, month, day, hour, minute, second, millisecond,
                                  magnitude, latitude, longitude, depth]
                    csv_writer.writerow(output_row)

# main method that calls the web scraper function
if __name__ == "__main__":
    file_directory = "src/scraper/NCEDC/raw/double_difference_"

    # find all the input path txts
    input_paths = []
    
    # the raw folder contains all txt files for earthquake data
    for k in range(1984, 2024):
        file_name = file_directory + str(k) + ".txt"
        input_paths.append(file_name)

    # set the output path where the combined csv file will be stored
    output_filename = "NCEDC (1984-2023)"
    output_path = f"src/scraper/NCEDC/clean/{output_filename}.csv"
    
    # find the earthquakes then clean the data
    find_quakes(input_paths, output_path)
    clean_data(output_path)
