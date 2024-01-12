# run on python 3.11.2
from csv import writer

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(input_path: str, output_path: str):
    
    with open(input_path, "r") as input_file:
        with open(output_path, "w") as out_file:

            # label the header of the csv with the appropriate labels
            csv_writer = writer(out_file, lineterminator="\n")
            header = ["Year", "Month", "Day", "Hour", "Minute", "Second", "ET", "GT",
                      "Magnitude", "M", "Latitude", "Longitude", "Depth",
                      "Q", "EVID", "NPH", "NGRM"]
            csv_writer.writerow(header)
            for i in range(3): next(input_file, None)

            # write each row from the txt file to the csv
            for line in input_file:
                words = line.split()

                try:
                    # put each time unit (excluding ms) in separate columns
                    year, month, day = words[0].split("/")
                    hour, minute, second = words[1].split(":")
                    second = second[:2]

                    # convert them into integers
                    year, month, day = int(year), int(month), int(day)
                    hour, minute, second = int(hour), int(minute), int(second)

                    # reformat the line
                    words = [year, month, day, hour, minute, second] + words[2:]
                    csv_writer.writerow(words)
                
                except Exception as e:
                    print(str(e))

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/SoCal/SearchResults.txt"
    output_path = "src/scraper/SoCal/Southern California Earthquakes (1932-2023).csv"
    find_quakes(input_path, output_path)
