# run on python 3.11.2
from bs4 import BeautifulSoup
import requests
from csv import writer

# scrapes a url and outputs the data as a CSV file
def find_quakes(url: str, output_path: str):
    
    # access the website using BeatifulSoup and requests
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    # open a new csv file in the output path to write data into
    with open(output_path, "w", newline="", encoding="utf8") as f:

        # the header labels each column for readability
        csv_writer = writer(f, lineterminator="\n")
        header = ["Year/Month/Day", "Hour:Minute:Second", "ET", "GT",
                  "Magnitude", "M", "Latitude", "Longitude", "Depth",
                  "Q", "EVID", "NPH", "NGRM"]
        # csv_writer.writerow(header)

        # find the earthquakes stored in the website's table (accessed via html <body> tag)
        quakes = soup.find("body").text
        rows = quakes.split("\n")

        # only add rows with earthquake data by checking its length with the header
        for row in rows:
            data = row.split()
            if len(data) == len(header):
                csv_writer.writerow(data)

# main method that calls the web scraper function
if __name__ == "__main__":
    target_site = "https://service.scedc.caltech.edu/cgi-bin/catalog/catalog_search.pl?outputfmt=scec&start_year=1932&start_month=01&start_day=01&start_hr=00&start_min=00&start_sec=00&end_year=2023&end_month=07&end_day=25&end_hr=00&end_min=00&end_sec=00&min_mag=1&max_mag=9.9&min_depth=0&max_depth=1000.0&south_latd=30.0&north_latd=39.0&west_long=-124.0&east_long=-111.0&etype=eq&gtype=l&file_out=N"
    output_path = "SoCal/Southern California Earthquakes (1932-2023).csv"
    find_quakes(target_site, output_path)