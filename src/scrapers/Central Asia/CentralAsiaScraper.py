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
                words = line.split(",")

                try:
                    # put each time unit (excluding ms) in separate columns
                    year, month, day = words[1], words[2], words[3]
                    hour, minute, second = words[4], words[5], words[6]

                    # convert them into integers
                    year = int(year)
                    month = int(month) if month != "NA" else 1
                    day = int(day) if day != "NA" else 1
                    hour = int(hour) if hour != "NA" else 1
                    minute = int(minute) if minute != "NA" else 1
                    second = int(second) if second != "NA" else 1

                    # find the other rows with data
                    magnitude = float(words[10])
                    latitude = float(words[7])
                    longitude = float(words[8])
                    depth = float(words[9])

                    # reformat the line
                    data = [year, month, day, hour, minute, second,
                             magnitude, latitude, longitude, depth]
                    csv_writer.writerow(data)
                
                except Exception as e:
                    print(str(e))

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scrapers/Central Asia/EMCA Central Asia Earthquake Catalogue.csv"
    output_path = "src/scrapers/Central Asia/EMCA Central Asia.csv"
    find_quakes(input_path, output_path)
