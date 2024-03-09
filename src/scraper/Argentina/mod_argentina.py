import csv
import xmltodict
import sys
from pathlib import Path

# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

# Now you can import your module
from scraper.Scraper import Scraper



class argintina(Scraper):
    def __init__(self, input_path, output_path,header):
        self.input_path=input_path
        self.output_path=output_path
        self.header=header
    def find_quakes(self):
        with open(self.input_path, "r") as file:
            file_data = file.read()
        # find all 1436 events in the XML file
        data_dict = xmltodict.parse(file_data)
        data_list = data_dict["quakeml"]["eventParameters"]["event"]

        # find key data points for all earthquakes
        n = len(data_list)

        # collect each event's data in rows
        rows = []
        for row in data_list:
            time = row["origin"][0]["time"]["value"]
            mag = row["stationMagnitude"][0]["mag"]["value"]
            lat = row["origin"][0]["latitude"]["value"]
            lon = row["origin"][0]["longitude"]["value"]
            dep = row["origin"][0]["depth"]["value"]

            rows.append([time, mag, lat, lon, dep])

        # write the data into the csv file
        with open(self.output_path, "w") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(self.header)
            csv_writer.writerows(rows)

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "Argentina/clean-catalog.xml"
    output_path = "Argentina/Argentina Andean Earthquakes (2016-2017).csv"
    header = ["Time ID", "Magnitude", "Station Count", "Author", "Publication Time"]
    argintina=argintina(input_path, output_path,header)
    argintina.find_quakes()

    
    