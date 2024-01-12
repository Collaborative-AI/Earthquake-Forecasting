# run on python 3.11.2
from csv import writer
import numpy as np

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(input_path: str, output_path: str):
    
    with open(input_path, "r") as input_file:
        with open(output_path, "w") as out_file:

            # label the header of the csv with the appropriate labels
            csv_writer = writer(out_file, lineterminator="\n")
            header = ["Year", "Month", "Day", "Hour", "Minute", "Second",
                      "Magnitude", "Latitude", "Longitude", "Depth"]
            csv_writer.writerow(header)
            next(input_file, None)

            # write each row from the txt file to the csv
            for line in input_file:
                words = line.split(",")

                try:
                    # put each time unit (excluding ms) in separate columns
                    datetime = words[3].split(" ")
                    dummy, date, time = datetime

                    year, month, day = date.split("-")
                    hour, minute, second = time.split(":")

                    # convert them into integers
                    year, month, day = int(year), int(month), int(day)
                    hour, minute, second = int(hour), int(minute), int(second)

                    # convert the energy into moment magnitude (Mw)
                    # formula found at: https://www.usgs.gov/programs/earthquake-hazards/earthquake-magnitude-energy-release-and-shaking-intensity
                    # conversion: logE = 5.24 + 1.44(Mw)
                    energy = float(words[4])

                    # don't evaluate for energy = 0 to avoid a divide by zero error
                    if energy == 0: continue
                    magnitude = (np.emath.logn(10, energy)-5.24)/1.44

                    # find the other rows with data
                    latitude = words[0]
                    longitude = words[1]
                    depth = words[2]

                    # reformat the line
                    data = [year, month, day, hour, minute, second,
                             magnitude, latitude, longitude, depth]
                    csv_writer.writerow(data)
                
                except Exception as e:
                    print(str(e))

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/Pacific Northwest/pacific-northwest-tremors-2009-2023.csv"
    output_path = "src/scraper/Pacific Northwest/PNW Tremors (2009-2023).csv"
    find_quakes(input_path, output_path)
