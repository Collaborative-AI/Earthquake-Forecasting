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
            # label abbreviations: http://folkworm.ceri.memphis.edu/catalogs/html/cat_nm_help.html
            csv_writer = writer(out_file, lineterminator="\n")
            header = ["Year", "Month", "Day", "Hour", "Minute", "Second", "Millisecond",
                      "Magnitude", "Latitude", "Longitude", "Depth"]
            csv_writer.writerow(header)

            # write each row from the txt file to the csv
            for line in input_file:
                row = line.split()

                # find the year, month, day, hour, minute, and second
                # extract the date and time information from the rows
                year, month, day = row[1].split("/")
                year, month, day = int(year), int(month), int(day)

                # extract the hour, minute, and second
                time = row[2][:8]
                hour, minute, second = time.split(":")
                hour, minute, second = int(hour), int(minute), int(second)
                
                # extract the milliseconds
                millisecond = int(float(row[2][-5:]) * 1000)
                
                # extract other earthquake information
                magnitude = row[6]
                latitude = row[3]
                longitude = row[4]
                depth = row[5]
                
                # afterwards, write this information to the next row
                output_row = [year, month, day, hour, minute, second, millisecond,
                                  magnitude, latitude, longitude, depth]
                csv_writer.writerow(output_row)


# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/New Madrid/raw/New Madrid Earthquakes 1974-2023.txt"
    
    output_filename = "New Madrid (1974-2023)"
    output_path = f"src/scraper/New Madrid/clean/{output_filename}.csv"
    
    find_quakes(input_path, output_path)
    clean_data(output_path)
