# import helper functions for data cleaning
import sys
sys.path.append("src/scraper")
from helper import clean_data

# run on python 3.11.2
from csv import writer
import pandas as pd
import numpy as np

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
                    
                    # extract the data as a pd.Timestamp object
                    ts = pd.Timestamp(row[3])
                    
                    # extract time information from the timestamp
                    year = ts.year
                    month = ts.month
                    day = ts.day
                    hour = ts.hour
                    minute = ts.minute
                    second = ts.second
                    millisecond = ts.microsecond // 1000

                    # convert the energy into moment magnitude (Mw)
                    # formula found at: https://www.usgs.gov/programs/earthquake-hazards/earthquake-magnitude-energy-release-and-shaking-intensity
                    # conversion: logE = 5.24 + 1.44(Mw)
                    energy = float(row[4])

                    # don't evaluate for energy = 0 to avoid a divide by zero error
                    if energy == 0: continue
                    magnitude = (np.emath.logn(10, energy)-5.24)/1.44

                    # find the other rows with data
                    latitude = row[0]
                    longitude = row[1]
                    depth = row[2]
                    
                    output_row = [year, month, day, hour, minute, second, millisecond,
                                  magnitude, latitude, longitude, depth]
                    csv_writer.writerow(output_row)
                
                except Exception as e:
                    print(str(e))


# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/Pacific Northwest/raw/pacific-northwest-tremors-2009-2023.csv"
    
    output_filename = "PNW Tremors (2009-2023)"
    output_path = f"src/scraper/Pacific Northwest/clean/{output_filename}.csv"
    
    find_quakes(input_path, output_path)
    clean_data(output_path)