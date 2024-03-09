import sys
# run on python 3.11.2
from pathlib import Path
from csv import writer
# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

# Now you can import your module
from scraper.Scraper import Scraper

class NOAA_Scraper(Scraper):
    def __init__(self, input_path, output_path, header, separator):
        self.input_path=input_path
        self.output_path=output_path
        self.header=header
        self.separator=separator
    
    # converts a txt file (separated by whitespace) to a csv file
    def find_quakes(self):
        with open(self.input_path, "r") as input_file:
            with open(self.output_path, "w") as out_file:

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