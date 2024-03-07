# run on python 3.11.2
from bs4 import BeautifulSoup
import requests
from csv import writer

# scrapes a url and outputs the data as a CSV file
def find_quakes(url: str):
    
    # access the website using BeatifulSoup and requests
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    # open a new csv file in a new folder (SRCMOD/srcmod.csv) to write data into
    with open("SRCMOD/srcmod.csv", "w", newline="", encoding="utf8") as f:

        # the header labels each column for readability
        csv_writer = writer(f)
        header = ["Earthquake ID", "Region", "Date (dd/mm/yyyy)", "Filnn-Engdahl Region", \
                " ", "Magnitude", "Latitude (°N)", "Longitude (°E)", "Depth (km)", \
                "Author", "Upload Date (mm/yyyy)"]
        csv_writer.writerow(header)

        # find the earthquakes stored in the website's table (accessed via html <table> tag)
        # for each row's (<tr>) cell (<td>), add the data into a list then append it into the CSV
        quakes = soup.find("table")
        rows = quakes.find_all("tr")
        for row in rows:
            quake_data = []
            for cell in row.find_all("td"):
                quake_data.append(cell.text.strip())
            csv_writer.writerow(quake_data)

# main method that calls the web scraper function
if __name__ == "__main__":
    srcmod_site = "http://equake-rc.info/SRCMOD/searchmodels/allevents/"
    find_quakes(srcmod_site)