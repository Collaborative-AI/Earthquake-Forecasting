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
            next(input_file, None)
            
            # keep track of the line number for exception tracking
            # starts at 1 since we skipped the header
            line_number = 1

            # write each row from the txt file to the csv
            for line in input_file:
                row = line.split(",")

                try:
                    # put each time unit (excluding ms) in separate columns
                    year, month, day = row[1], row[2], row[3]
                    hour, minute, second = row[4], row[5], row[6]

                    # convert them into integers
                    year = int(year)
                    month = int(month) if month != "NA" else 1
                    day = int(day) if day != "NA" else 1
                    hour = int(hour) if hour != "NA" else 0
                    minute = int(minute) if minute != "NA" else 0
                    second = int(second) if second != "NA" else 0
                    
                    # this dataset doesn't include millisecond, but we'll manually
                    # add 0s for consistency when merging with other datasets
                    millisecond = 0

                    # find the other rows with data
                    magnitude = float(row[10])
                    latitude = float(row[7])
                    longitude = float(row[8])
                    depth = float(row[9]) if row[9] != "NA" else None

                    # reformat the line
                    output_row = [year, month, day, hour, minute, second, millisecond,
                                  magnitude, latitude, longitude, depth]
                    csv_writer.writerow(output_row)
                
                except Exception as e:
                    print(f"At line {line_number}: {str(e)}")
            
                # update the row number by 1
                line_number += 1
        
# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/Central Asia/raw/EMCA Central Asia Earthquake Catalogue.csv"
    
    output_filename = "EMCA Central Asia (10-2009).txt"
    output_path = f"src/scraper/Central Asia/clean/{output_filename}.csv"
    
    find_quakes(input_path, output_path)
    clean_data(output_path)
