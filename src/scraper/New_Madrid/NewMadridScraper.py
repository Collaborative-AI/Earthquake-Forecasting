# run on python 3.11.2
from csv import writer

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(input_path: str, output_path: str):
    with open(input_path, "r") as input_file:
        with open(output_path, "w") as out_file:

            # label the header of the csv with the appropriate labels
            # label abbreviations: http://folkworm.ceri.memphis.edu/catalogs/html/cat_nm_help.html
            csv_writer = writer(out_file, lineterminator="\n")
            header = ['NET', 'DATE', 'O.T. (UTC)', 'LAT', 'LONG', 'DEP', \
                      'MAG', 'NPH', 'GAP', 'DMIN', 'RMS', 'SEO', 'SEH', 'SEZ',
                      'Q', 'COMMENTS']
            numCols = len(header)
            csv_writer.writerow(header)

            # write each row from the txt file to the csv
            for line in input_file:
                words = line.split()

                # the last column -- COMMENTS -- can consist of multiple words
                # if so, join the comments together with spaces and put them into one cell
                if len(words) > numCols:
                    words = words[:numCols-1] + [" ".join(words[numCols-1:])]
                
                # afterwards, write these words into the next row
                csv_writer.writerow(words)

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "New_Madrid/New Madrid Earthquakes 1974-2023.txt"
    output_path = "New_Madrid/New Madrid Earthquakes 1974-2023.csv"
    find_quakes(input_path, output_path)
