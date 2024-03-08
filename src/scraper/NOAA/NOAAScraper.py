# import helper functions for data cleaning
import sys
sys.path.append("src/scraper")

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
            for i in range(2): next(input_file, None)

            # write each row from the txt file to the csv
            for line in input_file:
                row = line.split("\t")
                
                # extract time information from each row
                year = int(row[1])
                month = int(row[2]) if row[2] else 1
                day = int(row[3]) if row[3] else 1
                hour = int(row[4]) if row[4] else 0
                minute = int(row[5]) if row[5] else 0
                
                # the "Sec" column in the dataset is a float that contains
                # both second and millisecond information
                total_millisecond = float(row[6]) * 1000 if row[6] else 0
                second, millisecond = divmod(total_millisecond, 1000)
                
                # extract geographic information about the earthquake
                magnitude = row[13]
                latitude = row[10]
                longitude = row[11]
                depth = row[12]
                
                # afterwards, write this information to the next row
                output_row = [year, month, day, hour, minute, second, millisecond,
                                  magnitude, latitude, longitude, depth]
                csv_writer.writerow(output_row)


# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/NOAA/raw/NCEI-WDS-Earthquakes.tsv"
    
    output_filename = "NOAA NCEI-WDS (0-2023)"
    output_path = f"src/scraper/NOAA/clean/{output_filename}.csv"
    
    find_quakes(input_path, output_path)
    clean_data(output_path)
