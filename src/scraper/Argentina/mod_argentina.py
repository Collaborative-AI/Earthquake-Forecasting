import csv
import xmltodict
import sys
from pathlib import Path

# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

# Now you can import your module
from Superclass import Scraper



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
            magnitude = row["stationMagnitude"][0]["mag"]["value"]
            stationCount = row["magnitude"]["stationCount"]
            author = row["magnitude"]["creationInfo"]["author"]
            creationTime = row["magnitude"]["creationInfo"]["creationTime"]

            rows.append([time, magnitude, stationCount, author, creationTime])

        # write the data into the csv file
        with open(self.output_path, "w") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(self.header)
            csv_writer.writerows(rows)

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "Argentina/raw/clean-catalog.xml"
    output_path = "Argentina/clean/Argentina Andean Earthquakes (2016-2017).csv"
    header = ["Time ID", "Magnitude", "Station Count", "Author", "Publication Time"]
    argintina=argintina(input_path, output_path,header)
    argintina.find_quakes()

    
    