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

                # find the separate values from the time
                year = row[0]
                time, millisecond = row[1].split(".")
                stamps = [time[max(0, k-2):k] for k in range(len(time), -1, -2)]
                second, minute, hour, day, month = stamps[:5]

                # find the remaining values
                magnitude = row[5]
                latitude = row[2]
                longitude = row[3]
                depth = row[4]

                # write the row into the result csv
                output_row = [year, month, day, hour, minute, second, millisecond,
                              magnitude, latitude, longitude, depth]
                csv_writer.writerow(output_row)

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/Corinth/raw/Marathias_seq.txt"
    
    output_filename = "Corinth Gulf (2020-2021)"
    output_path = f"src/scraper/Corinth/clean/{output_filename}.csv"
    
    find_quakes(input_path, output_path)
    clean_data(output_path)
