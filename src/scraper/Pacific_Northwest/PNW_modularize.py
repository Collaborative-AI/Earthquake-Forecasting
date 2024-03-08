import sys
# run on python 3.11.2
from pathlib import Path
from csv import writer
import pandas as pd
import numpy as np
# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

# Now you can import your module
from scraper.Scraper import Scraper

class PNW_Scraper(Scraper):
    def __init__(self, input_path, output_path):
        self.input_path=input_path
        self.output_path=output_path

    def find_quakes(self):
        
        with open(self.input_path, "r") as input_file:
            with open(self.output_path, "w") as out_file:

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