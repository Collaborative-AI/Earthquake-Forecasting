# import helper functions for data cleaning
import sys
sys.path.append("src/scraper")
from helper import clean_data

# run on python 3.11.2
from csv import writer

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(input_path: str, output_path: str):
    
    with open(input_path, "r") as input_file:
        with open(output_path, "w") as out_file:

            # label the header of the csv with the appropriate labels
            csv_writer = writer(out_file, lineterminator="\n")
            header = ["Year", "Month", "Day", "Hour", "Minute", "Second", "Millisecond",
                      "Magnitude", "Latitude", "Longitude", "Depth"]
            csv_writer.writerow(header)

            # write each row from the txt file to the csv
            for line in input_file:
                row = line.split()

                # find the date by splitting it every two chars
                year = int(row[0])
                date = row[1]
                month, day, hour, minute, second = [int(date[2*k:2*k+2]) for k in range(5)]
                millisecond = int(float(date[-3:]) * 1000)
                
                # extract the geographical information
                magnitude = row[6]
                latitude = row[2]
                longitude = row[3]
                depth = row[4]
                
                # cast from strings to ints
                output_row = [year, month, day, hour, minute, second, millisecond,
                                  magnitude, latitude, longitude, depth]
                csv_writer.writerow(output_row)


# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/Utah/raw/detections.txt"
    
    output_filename = "Utah (2016-2019)"
    output_path = f"src/scraper/Utah/clean/{output_filename}.csv"
    
    find_quakes(input_path, output_path)
    clean_data(output_path)
    