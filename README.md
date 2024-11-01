# SmartQuake

SmartQuake is a research project to predict earthquake on a global scale with the latest machine learning technologies. It incorporates data from 14 datasets from worldwide, creating a dataset that can also be used for future research in earthquake prediction. 

# Dataset Scraping

## Scraping the dataset
- From the Google Drive, download the raw datasets. The datasets should be placed respectively under `src/scraper/.../raw` folder.
- After installing the dependencies by `pip install requirements.txt`, run `python src/main.py`
- The scraped datasets will be placed under the path `src/scraper/.../clean`

# Data Processing

## Earthquake Dataset Merger

## Overview
This tool merges various earthquake catalogs from different geographical regions into a single, worldwide dataset. The output is a CSV file that is sorted chronologically and contains no duplicates.

## Requirements
- Python 3.11.2

## Setup
1. Ensure Python 3.11.2 is installed on your system.
2. Clone the repository to your local machine.

## Dataset checkpoints

From these links we can access the checkpoints of the multiple stages of the dataset acquisition process:

Scraper: https://drive.google.com/drive/folders/1okZ_2QW58CqQwPA8JIDIwmaBbcOtLIMp?usp=sharing

Preprocessed: https://drive.google.com/drive/folders/1CnXaP9KgUxgQrrreYt3s1MSbCJKHmCQy?usp=sharing

Merged (finalized) dataset: https://drive.google.com/drive/folders/1GUvjtBC2jBqHQGbAVy4rqSAd9fXe3sxT?usp=sharing

## Details of the data generation process

## Scraping

### Overview
This script is designed to scrape earthquake data from various sources including text files, web pages, and PDFs. It utilizes BeautifulSoup for web scraping, Pandas for data manipulation, and Tabula for PDF data extraction.

### Installation
To run this script, you need Python 3.x and the following packages:
- BeautifulSoup4
- requests
- pandas
- tabula-py

Install them using pip: pip install beautifulsoup4 requests pandas tabula-py

### Usage

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
```

## Data Processing

Data processing is the **second step** of the SmartQuake data pipeline as shown above. After scraping all the datasets from the set of selected earthquake observatories, we need to compile all the CSVs into a standardized format, such that all datasets share the exact same columns.

Running data processing ensures that all SmartQuake earthquake CSVs have these 5 columns:

- **Timestamp ⏱️**
  - Stored as a `pd.Timestamp` string formatted as (YYYY-MM-DD HH:MM:SS.millisecond+00:00)
  - All times are set to UTC
  - Example: (2016-06-17 03:31:29.459000+00:00)
- **Magnitude 📈**
  - Uses **moment** magnitude (Mw)
  - No other magnitude types are included (e.g., Md, Richter)
- **Latitude 🌏**
  - Guaranteed to be within [-90, 90]
- **Longitude 🌍**
  - Guaranteed to be within [-180, 180]
- **Depth 📏**
  - Represented in kilometers (km)
  - For example, `depth=2.6` means the earthquake occurred 2.6 km below sea level.
  - **Warning:** This is an "optional" column, meaning that NOT all rows have a depth value. In other words, it's possible for `depth=None`, especially for older earthquake records (i.e., pre-20th century).

Furthermore, all datasets store earthquakes in **chronological order**, and feature **no duplicates** within each individual CSV.

### **File Organization 📜**

The `data_processing/` folder has two key files and one key folder that are required to run the data processing code.

- [data_processor.py](data_processor.py):
  - Contains the `DataProcessor` class that handles standardizes data processing for all datasets with just one function.
- [run_processor.py](run_processor.py):
  - Runs the `DataProcessor` functions for all scraped datasets.
- **processed/**: 
  - Folder that contains the processed output datasets (CSVs)
  - If, for some reason, this folder doesn't exist, make sure to create one.

### **Running Data Processing 🏃**

Data processing is a simple process that involves verifying input and output paths, and simply running a Python file.

### **Step 1: Compiling the Scraped Datasets**

The `data_processing/` folder assumes that the scraper code has already been run. If not, read the `scraper/` folder [`README.txt`](../scraper/README.md) first. Before moving to the next step, make sure that all `clean` datasets have the required datasets as expected.

### **Step 2: Confirm the processed/ folder exists**

The `processed/` folder will contain the output files that convert scraped datasets into processed datasets. Make sure that `data_processing/processed/` exists, or you'll likely run into a runtime error.

### **Step 3: Run run_processor.py**

If all the input and output filepaths were linked properly, then `run_processor.py` should be able to call the `DataProcessor` class and ensure that all datasets have the same 5 columns as described prior.

### **Step 4: Completion**

Confirm that all your CSVs exist in the `processed/` folder after running the data processing code. Afterwards, you should be able to move on to the next step of the data pipeline: merging datasets.

## Merging

Merging is the **third step** of the SmartQuake data pipeline as shown above. After processing all the datasets from the set of selected earthquake observatories, we need to merge all the CSVs into one big file, which can thne serve as input data for a machine learning model.

Running the merge code preserves the same 5 columns featured in the data processing datasets. Once again, the merged dataset stores earthquakes in **chronological order**, and features **no duplicates**.

### **File Organization 📜**

The `merge/` folder has four key files and two key folders that are required to run the data processing code.

- [helper.py](helper.py):
  - Provides helper functions for `merge.py`, mainly to merge multiple CSVs into one
- [merge.py](merge.py):
  - Merges all non-USGS/SAGE datasets into a CSV titled `Various-Catalogs.csv`
- **usgs_pre_1950/**: 
  - [usgs_merge.py](usgs_pre_1950/usgs_merge.py):
    - Merges USGS datasets into one CSV
  - [preprocess.py](usgs_pre_1950/preprocess.py):
    - Preprocesses USGS datasets before running `usgs_merge.py`
- **final/**:
  - [usgs_sage_various_merge.py](final/usgs_sage_various_merge.py):
    - Merges non-USGS/SAGE dataset with the USGS/SAGE dataset
    - Outputs `Completed-Merge.csv`, which can be used for machine learning model input

### **Running Merge 🏃**

Data processing is a simple process that involves verifying input and output paths, and simply running a Python file.

### **Step 1: Compiling the Processed Datasets**

Ensure that all processed datasets are contained in the `data_processing/processed/` directory. This filepath should not contain any USGS or SAGE datasets. If you have not either [scraped](../scraper/README.md) or [processed](../data_processing/README.md) the code, complete both steps before doing so.

### **Step 2: First Merge**

Run `merge.py` to merge the datasets in the `processed/` folder. This should combine all of those datasets into a file titled `Various-Catalogs.csv`.

### **Step 3: Processing and Merging USGS Data**

Now that all the non-USGS/SAGE data has been compiled into one dataset, we now have to process and merge the USGS data. Download the [USGS](https://drive.google.com/drive/folders/1mcT7pdQ73oZAeLJR5NoC4HtXwkFjOCH9?usp=drive_link) and [SAGE](https://drive.google.com/drive/folders/1A1qYsD_WXZRmvcUdYRn-JbqdMk3sVC3O?usp=drive_link) datasets from the Google Drive and store the files in `merge/usgs_pre_1950`. Then, run `preprocess.py` and `merge.py` to create `USGS_SAGE_Merged.csv`.

If you want to speed this process, or have run into any bugs, you can skip this step by visiting the Google Drive to and directly downloading [`USGS_SAGE_Merged.csv`](https://drive.google.com/file/d/1vZxxrXIYR7K7YWcuJUe4HGYJH8vDCTpX/view?usp=drive_link). Store the file in `merge/final/` for the next step.

### **Step 4: Final Merge**

Now that you have both the non-USGS/SAGE dataset and the USGS/SAGE dataset, you can run `usgs_sage_various_merge.py` to merge the two datasets together. The script uses a two-pointer approach to merge the two datasets into a combined file titled `Completed-Merge.csv`. This dataset can then be used to serve as input data for machine learning models.