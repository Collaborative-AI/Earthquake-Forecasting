# SmartQuake

SmartQuake is a research project to predict earthquake on a global scale with the latest machine learning technologies. It incorporates data from 14 datasets from worldwide, creating a dataset that can also be used for future research in earthquake prediction. 

# Data Collection 

## Unified Scraper

## Overview
The Unified Scraper is a flexible Python class designed to handle scraping tasks across various data formats including XML, TXT, TSV, and CSV files. It allows for easy configuration and extension to support a wide range of scraping needs.

## Features
- Supports multiple data types: XML, TXT, TSV, CSV
- Easy to add new scraper configurations
- Customizable for specific scraping requirements

## How to Use
1. Initialize the `UnifiedScraper` class.
2. Use the `add_scraper` method to add new scraper configurations as needed.
3. Call the `find_quakes` method to process all configured scrapers.

## Example
```python
scraper = UnifiedScraper()
scraper.add_scraper("path/to/input", "path/to/output", "data_type", ["Header1", "Header2"], ",", 0)
scraper.find_quakes()
```

## Example Adding a New Scraper Configuration

scraper.add_scraper(
    input_path="path/to/new/data",
    output_path="path/to/save/results",
    data_type="txt", # Or "xml", "csv", "tsv"
    header=["Column1", "Column2", "Column3"], # Optional
    separator=",", # Optional, default is ","
    num_skips=0 # Optional, lines to skip at the beginning of the file
)

## Dependencies

- Python 3.x
- xml.etree.ElementTree
- csv

Ensure all dependencies are installed and up to date in your Python environment to utilize the Unified Scraper effectively.

# Data Processing 

## Earthquake Dataset Merger

## Overview
This tool merges various earthquake catalogs from different geographical regions into a single, worldwide dataset. The output is a CSV file that is sorted chronologically and contains no duplicates.

## Requirements
- Python 3.11.2

## Setup
1. Ensure Python 3.11.2 is installed on your system.
2. Clone the repository to your local machine.

## Usage
1. Place all earthquake catalog datasets within the `src/data_processing/processed/` directory. Ensure that datasets from USGS and SAGE are excluded.

2. Run `merge.py` to merge the datasets:  [python merge.py]

3. The merged dataset will be saved to `src/merge/Various-Catalogs.csv`.

## Details
- The script first finds all the filepaths to datasets in the `src/data_processing/processed/` folder.
- It then uses the `merge_group` function from `src/merge/helper.py` to merge these files.
- The final output is stored in the `src/merge/` folder, ensuring the data is sorted and distinct.
