# run on python 3.11.2
from csv import writer

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(input_path: str, output_path: str):
    
    with open(input_path, "r", encoding='gb18030', errors='ignore') as input_file:
        with open(output_path, "w") as out_file:

            # label the header of the csv with the appropriate labels
            csv_writer = writer(out_file, lineterminator="\n")
            header = ["En", "Source", "Year", "Mo", "Da", "Ho", "Mi", "Se",
                      "Area", "Lat", "Lon", "LatUnc", "LonUnc", "EpDet", "Dep",
                      "Io", "Msource", "M", "MUnc", "MType", "MDet", "MDPSource",
                      "MDPn", "MDPIx", "MDPsc", "Remarks", "GEHid"]
            csv_writer.writerow(header)

            # write each row from the txt file to the csv
            for line in input_file:
                words = line.split("\t")
                csv_writer.writerow(words)

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "GHEA/raw/GHEA-data.txt"
    output_path = "GHEA/clean/GHEA Data 1000-1903.csv"
    find_quakes(input_path, output_path)
