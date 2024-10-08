import csv
import xmltodict


def find_quakes(input_path: str, output_path: str):
    
    # open the xml file
    with open(input_path, "r") as file:
        file_data = file.read()

    # find all 1436 events in the XML file
    data_dict = xmltodict.parse(file_data)
    data_list = data_dict["quakeml"]["eventParameters"]["event"]

    # find key data points for all earthquakes
    n = len(data_list)
    header = ["Time ID", "Magnitude", "Latitude", "Longitude", "Depth"]

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
    with open(output_path, "w") as f:
        csv_writer = csv.writer(f, lineterminator="\n")
        csv_writer.writerow(header)
        csv_writer.writerows(rows)

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/Argentina/raw/clean-catalog.xml"
    output_path = "src/scraper/Argentina/clean/Argentina Andean Earthquakes (2016-2017).csv"
    find_quakes(input_path, output_path)