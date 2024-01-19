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
            for i in range(79): next(input_file, None)

            # write each row from the txt file to the csv
            for line in input_file:
                row = line.split("\t")
                
                # check if the data has the magType "w". if not, skip
                # "w" = moment magnitude (for this dataset)
                if row[19].lower() != "w":
                    continue
                
                # find the time data
                year = row[2]
                month = row[3]
                day = row[4]
                hour = row[5]
                minute = row[6]
                second = row[7]
                millisecond = 0
                
                # find other earthquake attribute data
                magnitude = row[17]
                latitude = row[9]
                longitude = row[10]
                depth = row[14]
                
                # add the output row to the csv
                output_row = [year, month, day, hour, minute, second, millisecond,
                                  magnitude, latitude, longitude, depth]
                csv_writer.writerow(output_row)

    
# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/GHEA/raw/GHEA-data.txt"
    
    output_filename = "GHEA (1000-1903)"
    output_path = f"src/scraper/GHEA/clean/{output_filename}.csv"
    
    find_quakes(input_path, output_path)
    clean_data(output_path)
