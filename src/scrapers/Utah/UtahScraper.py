# run on python 3.11.2
from csv import writer

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(input_path: str, output_path: str):
    
    with open(input_path, "r") as input_file:
        with open(output_path, "w") as out_file:

            # label the header of the csv with the appropriate labels
            csv_writer = writer(out_file, lineterminator="\n")
            header = ["Year", "Month", "Day", "Hour", "Minute", "Second", "Latitude", "Longitude",
                      "Depth", "Template Event Magnitude", "Detection Magnitude",
                      "Event Template ID", "Detection ID", "Correlation Coefficient"]
            csv_writer.writerow(header)

            # write each row from the txt file to the csv
            for line in input_file:
                words = line.split()

                # find the date by splitting it every two chars
                date = words[1]
                month, day, hour, minute, second = [date[2*k:2*k+2] for k in range(5)]

                # cast from strings to ints
                year, month, day = int(words[0]), int(month), int(day)
                hour, minute, second = int(hour), int(minute), int(second)

                # update the row's values
                words = [year, month, day, hour, minute, second] + words[2:]
                csv_writer.writerow(words)

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scrapers/Utah/detections.txt"
    output_path = "src/scrapers/Utah/Mineral Mountains, Utah 2016-19.csv"
    find_quakes(input_path, output_path)
