# run on python 3.11.2
from csv import writer

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(input_path: str, output_path: str):
    with open(input_path, "r") as input_file:
        with open(output_path, "w") as out_file:

            # label the header of the csv with the appropriate labels
            # label abbreviations: http://folkworm.ceri.memphis.edu/catalogs/html/cat_nm_help.html
            csv_writer = writer(out_file, lineterminator="\n")
            header = ["Year", "Month", "Day", "Hour", "Minute", "Second",
                      'LAT', 'LONG', 'DEP', 'MAG', 'NPH', 'GAP', 'DMIN',
                      'RMS', 'SEO', 'SEH', 'SEZ', 'Q', 'COMMENTS']
            numCols = 16
            csv_writer.writerow(header)

            # write each row from the txt file to the csv
            for line in input_file:
                words = line.split()

                # the last column -- COMMENTS -- can consist of multiple words
                # if so, join the comments together with spaces and put them into one cell
                if len(words) > numCols:
                    words = words[:numCols-1] + [" ".join(words[numCols-1:])]

                # find the year, month, day, hour, minute, and second
                # extract the date and time information from the rows
                year, month, day = words[1].split("/")
                year, month, day = int(year), int(month), int(day)

                # extract the hour, minute, and second
                time = words[2][:8]
                hour, minute, second = time.split(":")
                hour, minute, second = int(hour), int(minute), int(second)

                # update the row with the new date and time columns
                datetime = [year, month, day, hour, minute, second]
                
                # afterwards, write these words into the next row
                words = datetime + words[3:]
                csv_writer.writerow(words)
                

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scrapers/New Madrid/New Madrid Earthquakes 1974-2023.txt"
    output_path = "src/scrapers/New Madrid/New Madrid Earthquakes 1974-2023.csv"
    find_quakes(input_path, output_path)
