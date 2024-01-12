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

            # write each row from the txt file to the csv
            for line in input_file:
                words = line.split()

                # find the separate values from the time
                year = words[0]
                time = words[1]
                if "." in time: time = time[:time.index(".")]
                stamps = [time[max(0, k-2):k] for k in range(len(time), -1, -2)]
                second, minute, hour, day, month = stamps[:5]

                # find the remaining values
                mag = words[5]
                lat = words[2]
                lon = words[3]
                dep = words[4]

                # write the row into the result csv
                row = [year, month, day, hour, minute, second, mag, lat, lon, dep]
                csv_writer.writerow(row)

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scrapers/Corinth/Marathias_seq.txt"
    output_path = "src/scrapers/Corinth/Corinth Gulf 2020-21 Seismic Crisis.csv"
    find_quakes(input_path, output_path)
