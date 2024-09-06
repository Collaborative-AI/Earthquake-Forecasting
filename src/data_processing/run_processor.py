from data_processor import DataProcessor
from tqdm import tqdm

"""
Initialization

Create DataProcessor objects for all the datasets used for the final dataset.
For more information on how DataProcessor is initialized, see data_processor.py
"""
argentina         = DataProcessor(datetime=[0], mag=1, lat=2, long=3, depth=4)
canada            = DataProcessor(datetime=[1], mag=6, mag_type=5, mag_letter="mw",
                                  lat=2, long=3, depth=4)
east_africa       = DataProcessor(datetime=[6], mag=1, lat=7, long=8, depth=9)
ghea              = DataProcessor(year=2, month=3, day=4, hour=5, minute=6, second=7,
                                  mag=17, mag_type=19, mag_letter="w", lat=9, long=10, depth=14)
intensity         = DataProcessor(datetime=[0,1,2,3,4,5], local_tz=6, mag=10,
                                  lat=8, long=9, depth=11)
japan             = DataProcessor(datetime=[0,1], mag=5, lat=2, long=3, depth=4, global_tz="Japan")
noaa              = DataProcessor(year=1, month=2, day=3, hour=4, minute=5, second=6,
                                  mag=13, lat=10, long=11, depth=12)
pacific_northwest = DataProcessor(datetime=[3], lat=0, long=1, depth=2, energy=4)
socal             = DataProcessor(datetime=[0,1], mag=4, lat=6, long=7, depth=8)
south_asia        = DataProcessor(year=0, month=1, day=2, hour=3, minute=4, second=5,
                                  mag=9, lat=6, long=7, depth=8)
texas             = DataProcessor(datetime=[2,3], mag=5, lat=6, long=8, depth=10)
turkey            = DataProcessor(datetime=[2,3], mag=10, lat=4, long=5, depth=6)
world_tremor      = DataProcessor(datetime=[0,1], mag=5, lat=2, long=3, depth=4)

"""
Finding Filepaths

Collect all the data processors in a list. Similarly, collect input and output paths in lists.
All three lists should have the same length, with each index corresponding to another.
"""
processors = [argentina, canada, east_africa, ghea, intensity, japan, noaa,
              pacific_northwest, socal, south_asia, texas, turkey, world_tremor]

# First, find all the file names for the input and output files.
filenames = [
             "Argentina Andean Earthquakes (2016-2017).csv",
             "Canada (1985-2024).csv",
             "East Africa Rift System (1994-2022).csv",
             "GHEA (1000-1903).csv",
             "U.S. Earthquake Intensity Database (1638-1985).csv",
             "Japan Database (2005-2014).csv",
             "NOAA NCEI-WDS (0-2024).csv",
             "PNW Tremors (2009-2024).csv",
             "SCEDC (1932-2024).csv",
             "South Asia (1900-2014).csv",
             "Texas (2016-2023).csv",
             "Turkey (1915-2021).csv",
             "World Tremor Database (2005-2014).csv"
            ]

# Then, initialize the source paths for all the unprocessed files.
source_paths = [
                "src/scraper/Argentina/clean/",
                "src/scraper/Canada/clean/",
                "src/scraper/East_Africa/clean/",
                "src/scraper/GHEA/clean/",
                "src/scraper/Intensity/clean/",
                "src/scraper/World_Tremor/clean/",
                "src/scraper/NOAA/clean/",
                "src/scraper/Pacific_Northwest/clean/",
                "src/scraper/SoCal/clean/",
                "src/scraper/South_Asia/clean/",
                "src/scraper/Texas/clean/",
                "src/scraper/Turkey/clean/",
                "src/scraper/World_Tremor/clean/"
               ]

# Also, set the output folder name
output_folder = "src/data_processing/processed/"

# Now, we can create input and output file paths for all the 
input_paths =  [source_paths[i] + filenames[i] for i in range(len(source_paths))]
output_paths = [output_folder   + filenames[i] for i in range(len(source_paths))]

"""
Running the Processor

Now that we have the DataProcessor objects and the input/output filepaths, we can run
the data processing part of the project.
"""
for i in tqdm(range(len(input_paths))):
    processor = processors[i]
    filename = filenames[i]
    input_path = input_paths[i]
    output_path = output_paths[i]
    
    try:
        # Try to process the file and clean the data
        processor.process_quakes(filename, input_path, output_path)
        processor.clean_data(output_path)
    except Exception as e:
        # If there's an error, print the error and continue with the next file
        print(f"Error processing file: {filename}. Error: {e}")
        continue  # Move on to the next file