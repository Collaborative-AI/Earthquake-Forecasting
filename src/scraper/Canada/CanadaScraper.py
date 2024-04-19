# run on python 3.11.2
from csv import writer

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(input_path: str, output_path: str):
    
    with open(input_path, "r") as input_file:
        with open(output_path, "w") as out_file:

            # label the header of the csv with the appropriate labels
            csv_writer = writer(out_file, lineterminator="\n")

            # write each row from the txt file to the csv
            for line in input_file:
                words = line[:-2].split("|")
                csv_writer.writerow(words)

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/Canada/raw/Canada-19850101-20240412.txt"
    output_path = "src/scraper/Canada/clean/Canada (1985-2024).csv"
    find_quakes(input_path, output_path)
