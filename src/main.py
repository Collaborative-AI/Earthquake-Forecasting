# import all scraper functions
import sys
from scraper import *
import os

"""
main.py
Running this program will run all scrapers featured in the SmartQuake project.
"""

# define the relative path based on your current working directory
RELATIVE_PATH = "src/scraper/"

if __name__ == "__main__":
    
    # Syria
    '''
    syria=Syria_Scraper(RELATIVE_PATH + "Ancient/Syria/The historical earthquakes of Syria.pdf", RELATIVE_PATH + "Ancient/Syria/SyriaHistoricalEarthquakes.csv")
    syria.find_quakes()
    
    # Wikipedia
    wikipedia=Wiki_Scraper('https://en.wikipedia.org/wiki/List_of_historical_earthquakes', RELATIVE_PATH + 'Ancient/Wikipedia/WikiHistoricalEarthquakes.csv')
    wikipedia.find_quakes()
    
    # Argentina    
    argentina=Argentina_Scraper(RELATIVE_PATH+"Argentina/raw/clean-catalog.xml", RELATIVE_PATH+"Argentina/clean/Argentina Andean Earthquakes (2016-2017).csv")
    argentina.find_quakes()
    clean_data(RELATIVE_PATH+"Argentina/clean/Argentina Andean Earthquakes (2016-2017).csv")
    '''
    # Canada
    input_path = RELATIVE_PATH+"Canada/raw/Canada-19850109-20240119.txt"
    
    output_filename = "Canada (1985-2024)"
    output_path = RELATIVE_PATH + f"Canada/clean/{output_filename}.csv"
    
    Canada = Canada_Scraper(input_path, output_path)
    Canada.find_quakes()
    clean_data(output_path)