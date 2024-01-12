# run on python 3.11.2
from csv import writer

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
                words = line.split(";")

                try:
                    # put each time unit (excluding ms) in separate columns
                    year, month, day = words[2].split(".")
                    hour, minute, second = words[3].split(":")
                    second = second[:2]

                    # convert them into integers
                    year, month, day = int(year), int(month), int(day)
                    hour, minute, second = int(hour), int(minute), int(second)

                    # find the other rows with data
                    # NOTE: Magnitude is the maximum of various scales
                    # (e.g., MD, ML, Mw, Ms, Mb)
                    magnitude = float(words[7])
                    latitude = float(words[4])
                    longitude = float(words[5])
                    depth = float(words[6])

                    # reformat the line
                    data = [year, month, day, hour, minute, second,
                             magnitude, latitude, longitude, depth]
                    csv_writer.writerow(data)
                
                except Exception as e:
                    print(str(e))

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scrapers/Turkey/turkey_earthquakes(1915-2021).csv"
    output_path = "src/scrapers/Turkey/Turkey Earthquakes (1915-2021).csv"
    find_quakes(input_path, output_path)
