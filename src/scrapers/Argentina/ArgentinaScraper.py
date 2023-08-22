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
    header = ["Time ID", "Magnitude", "Station Count", "Author", "Publication Time"]

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
    with open(output_path, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header)
        csv_writer.writerows(rows)

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "Argentina/clean-catalog.xml"
    output_path = "Argentina/Argentina Andean Earthquakes (2016-2017).csv"
    find_quakes(input_path, output_path)