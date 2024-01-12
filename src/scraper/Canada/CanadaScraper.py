# run on python 3.11.2
from csv import writer

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(input_path: str, output_path: str):
    
    with open(input_path, "r") as input_file:
        with open(output_path, "w") as out_file:

            # label the header of the csv with the appropriate labels
            csv_writer = writer(out_file, lineterminator="\n")
            header = ["Year", "Month", "Day", "Hour", "Minute", "Second",
                      "Latitude", "Longitude", "Depth/km",
                      "MagType", "Magnitude", "EventLocationName"]
            csv_writer.writerow(header)
            next(input_file, None)

            # write each row from the txt file to the csv
            for line in input_file:
                words = line.split("|")

                # extract the date and time information from the rows
                date, time = words[1].split("T")

                # extract the year, month, and day
                year, month, day = date.split("-")
                year, month, day = int(year), int(month), int(day)

                # extract the hour, minute, and second
                time = time[:-5]
                hour, minute, second = time.split(":")
                hour, minute, second = int(hour), int(minute), int(second)

                # update the row with the new date and time columns
                datetime = [year, month, day, hour, minute, second]
                csv_writer.writerow(datetime + words[2:])

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/Canada/Canada-19850109-20230621.txt"
    output_path = "src/scraper/Canada/Canada-19850109-20230621.csv"
    find_quakes(input_path, output_path)
