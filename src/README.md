# Unified Scraper

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
