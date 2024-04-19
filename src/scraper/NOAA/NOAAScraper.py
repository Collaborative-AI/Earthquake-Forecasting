# import helper functions for data cleaning
import sys
sys.path.append("src/scraper")

# run on python 3.11.2
from csv import writer

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(input_path: str, output_path: str):
    with open(input_path, "r") as input_file:
        with open(output_path, "w") as out_file:

            # label the header of the csv with the appropriate labels
            # label abbreviations: http://folkworm.ceri.memphis.edu/catalogs/html/cat_nm_help.html
            csv_writer = writer(out_file, lineterminator="\n")

            # write each row from the txt file to the csv
            for line in input_file:
                row = line.split("\t")
                csv_writer.writerow(row)
    


# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/NOAA/raw/NOAA-20240412.tsv"
    
    output_filename = "NOAA NCEI-WDS (0-2024)"
    output_path = f"src/scraper/NOAA/clean/{output_filename}.csv"
    find_quakes(input_path, output_path)
