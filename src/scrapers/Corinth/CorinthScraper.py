# run on python 3.11.2
from csv import writer

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(input_path: str, output_path: str):
    
    with open(input_path, "r") as input_file:
        with open(output_path, "w") as out_file:

            # label the header of the csv with the appropriate labels
            csv_writer = writer(out_file, lineterminator="\n")
            header = ["Year", "Origin Time", "Latitude", "Longitude", "Depth",
                      "Magnitude", "Decimal Years", "Time Relative to First Earthquake",
                      "Event ID", "Cluster ID (sorted by #events)",
                      "Cluster ID (by time)", "Multiplet ID", "#events in Multiplet",
                      "E-W horizontal error", "N-S horizontal error",
                      "Vertical error"]
            csv_writer.writerow(header)

            # write each row from the txt file to the csv
            for line in input_file:
                words = line.split()
                csv_writer.writerow(words)

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "Corinth/Marathias_seq.txt"
    output_path = "Corinth/Corinth Gulf 2020-21 Seismic Crisis.csv"
    find_quakes(input_path, output_path)
