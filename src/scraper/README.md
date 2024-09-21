# **scraper/ ⚙️**

This folder contains documentation on how to run scrape earthquake datasets used for the SmartQuake earthquake forecasting project.

## **What does this folder do? 📁**

![SmartQuake Data Pipeline](../smartquake_pipeline.png)

Scraping is the **first step** of the SmartQuake data pipeline as shown above. From each individual earthquake observatory, we need to extract data from each source into a readable CSV, and we can grow this collection as input data for a machine learning model.

## **File Organization 📜**

The `scraper/` folder consists of subfolders denoting the name of the observatory that the CSVs have been scraped from. Each folder (except for the USGS folder) follows this schema:

- **Subfolder Name:**
  - **raw/**:
    - The raw extracted dataset from the earthquake observatory, in a non-CSV format
    - This folder doesn't exist if the original dataset is a CSV
  - **clean/**:
    - Formats the raw dataset as a CSV
  - [EARTHQUAKE_OBSERVATORY]Scraper.py
    - Scraper file that can individually scrape this earthquake observatory independently of the other observatories
  - [EARTHQUAKE_OBSERVATORY]_modularize.py
    - Modularized variant of the observatory scraper that is fitted to use with the modularized code.
  - README.md
    - Occasionally featured in a subfolder to denote additional details about the earthquake observatory, such as copyright information and when we last scraped it

Additionally, the `scraper/` folder also features two important files:

- [__init__.py](__init__.py):
  - File used to initialize the modularized scraper script
- [helper.py](helper.py):
  - File used to standardize the "cleaning" of scraper datasets
  - Used to convert `.catalog`, `.tsv`, and other non-CSV files into `.csv` files

## **Running Scraper 🏃**

Scraping can be automated by running the `main.py` script in the base folder of this repository.

### **Step 1: Importing the data files**

Visit the SmartQuake Google Drive to download the `scraper/` folder consisting of all the datafiles required to run the scraper code. Replace the `scraper/` folder in this repository with the pre-populated folder that you downloaded from Google Drive

### **Step 2: Run main.py**

You can run the scraping code with `main.py`, as featured in the base folder of this repository. Verify that the folder paths are formatted properly.

### **Step 3: Check the clean/ folders**

By the end of `main.py`, all the `clean/` subfolders for the `scraper/` folder should be populated with their respective CSVs. If there were no bugs running the program, it's a good sign that this process ran smoothly, and you can now move on to [data processing](../data_processing/README.md).

## **Credits and Contact: ☎️**

If you have problems running the scraper code, reach out to [Luke Nam](mailto:luke.nam@duke.edu), the author of this `README.md` and the code for merging the non-USGS/SAGE datasets.
