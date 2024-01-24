# import all scraper functions
import sys
sys.path.append("src/scraper/")
from scraper import *
import os

"""
main.py
Running this program will run all scrapers featured in the SmartQuake project.
"""

# define the relative path based on your current working directory
RELATIVE_PATH = "src/scraper/"

if __name__ == "__main__":
    
    # Argentina
    input_path = RELATIVE_PATH + "Argentina/raw/clean-catalog.xml"
    output_path = RELATIVE_PATH + "Argentina/clean/Argentina Andean Earthquakes (2016-2017).csv"
    find_quakes(input_path, output_path)
    clean_data(output_path)
    
    # Canada
    
    input_path = RELATIVE_PATH + "Canada/raw/Canada-19850109-20230621.txt"
    output_path = RELATIVE_PATH + "Canada/clean/Canada (1985-2023).csv"
    find_quakes(input_path, output_path)
    clean_data(output_path)