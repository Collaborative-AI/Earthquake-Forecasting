# run on python 3.11.2
from csv import writer

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(input_paths, output_path: str):
    
    with open(output_path, "w") as out_file:

        # label the header of the csv with the appropriate labels
        csv_writer = writer(out_file, lineterminator="\n")
        header = ["Year", "Month", "Day", "Hour", "Minute", "Second",
                      "Magnitude", "Latitude", "Longitude", "Depth"]
        csv_writer.writerow(header)
    
        # store all input data into one output file
        for input_path in input_paths:
            with open(input_path, "r") as input_file:

                # skip the header of the input file
                next(input_file, None)

                # write each row from the txt file to the csv
                for line in input_file:
                    words = line.split(",")

                    # extract the date and time information from the rows
                    date, time = words[0].split(" ")

                    # extract the year, month, and day
                    year, month, day = date.split("/")
                    year, month, day = int(year), int(month), int(day)

                    # extract the hour, minute, and second
                    time = time[:8]
                    hour, minute, second = time.split(":")
                    hour, minute, second = int(hour), int(minute), int(second)

                    # find the remaining columns
                    magnitude = words[4]
                    latitude = words[1]
                    longitude = words[2]
                    depth = words[3]

                    # reformat the line
                    data = [year, month, day, hour, minute, second,
                             magnitude, latitude, longitude, depth]
                    csv_writer.writerow(data)

# main method that calls the web scraper function
if __name__ == "__main__":
    file_directory = "src/scrapers/NCEDC/raw/double_difference_"

    # find all the input path txts
    input_paths = []
    
    # the raw folder contains all txt files for earthquake data
    for k in range(1984, 2024):
        file_name = file_directory + str(k) + ".txt"
        input_paths.append(file_name)

    # set the output path where the combined csv file will be stored
    output_path = "src/scrapers/NCEDC/NCEDC (1984-2023).csv"
    find_quakes(input_paths, output_path)
