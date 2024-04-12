# Earthquake Data Scraper

## Overview
This script is designed to scrape earthquake data from various sources including text files, web pages, and PDFs. It utilizes BeautifulSoup for web scraping, Pandas for data manipulation, and Tabula for PDF data extraction.

## Installation
To run this script, you need Python 3.x and the following packages:
- BeautifulSoup4
- requests
- pandas
- tabula-py

Install them using pip: pip install beautifulsoup4 requests pandas tabula-py

## Usage

1. **Initialization**: Create an instance of the `Scraper` class.
   - Parameters:
     - `input_path`: Path to the input file (for text and PDF sources).
     - `output_path`: Path where the output CSV will be saved.
     - `url`: URL of the webpage to scrape (for web sources).
     - `start_time` and `end_time`: Date range for filtering data.
     - `header`: List of column names for the output CSV.
     - `separator`: Character used to separate data in the input file (default is space for text files).

2. **Scraping**:
   - `find_quakes_txt(num_skips=0)`: For text files. `num_skips` allows skipping initial lines.
   - `find_quakes_web()`: For web pages. Scrapes data based on the body tag and predefined header.
   - `find_quakes()`: Placeholder for additional scraping methods.

3. **Example**:
```python
scraper = Scraper(input_path='input.txt', output_path='output.csv', url='http://example.com', header=['Date', 'Magnitude', 'Location'])
scraper.find_quakes_txt(num_skips=1)
scraper.find_quakes_web()