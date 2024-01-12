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

            # write each row from the txt file to the csv
            for line in input_file:
                row = line.split(",")

                try:
                    # put each time unit (excluding ms) in separate columns
                    # IRIS format splits date and time using T
                    datetime = row[6]
                    date, time = datetime.split("T")

                    # remove milliseconds from the time
                    time = time[:8]

                    # find the remaining values
                    year, month, day = date.split("-")
                    hour, minute, second = time.split(":")

                    # convert them into integers
                    year, month, day = int(year), int(month), int(day)
                    hour, minute, second = int(hour), int(minute), int(second)
                    
                    # add millisecond data for consistency with other datasets
                    millisecond = 0

                    # find the other rows with data
                    magnitude = row[3]
                    latitude = row[7]
                    longitude = row[8]
                    depth = row[9]

                    # reformat the line
                    output_row = [year, month, day, hour, minute, second, millisecond,
                                  magnitude, latitude, longitude, depth]
                    csv_writer.writerow(output_row)
                
                except Exception as e:
                    print(str(e))


# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/East Africa/raw/SouthEARS_EarthquakeCatalog.csv"
    
    output_filename = "East Africa Rift System (1994-2022)"
    output_path = f"src/scraper/East Africa/clean/{output_filename}.csv"
    
    find_quakes(input_path, output_path)
    clean_data(output_path)