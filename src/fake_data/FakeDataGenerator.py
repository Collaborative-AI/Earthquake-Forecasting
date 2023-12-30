# run on python 3.11.2
from csv import writer
import random
import math
import pandas as pd

# produces a set number of fake earthquake events
"""
Input:  num_events  -> integer specifying number of fake earthquake events to create
        output_path -> string filepath for output CSV file
Output: CSV file containing num_events fake earthquakes

Runs in O(nlogn) time and O(n) extra space
"""
def create_fake_data(num_events: int, output_path: str):
    
    with open(output_path, "w") as out_file:

        # label the header of the csv with the appropriate labels
        csv_writer = writer(out_file, lineterminator="\n")
        header = ["DateTime", "Magnitude", "Latitude", "Longitude", "Depth"]
        csv_writer.writerow(header)
        
        # store all the rows in the CSV
        # we'll write all of these at the end
        rows = []

        # generate a total of "num_events"
        for k in range(num_events):

            try:
                
                """
                STEP 1:
                Create a fake date for the earthquake.
                
                Use the random library in Python to generate these numbers. Remember
                to set a seed prior to using this library for reproducibility.
                
                Note that randint(a, b) is inclusive [a, b]. In other words, the numbers
                a and b can be generated.
                """
                
                year = random.randint(0, 2023)
                month = random.randint(1, 12)
                day = random.randint(1, 28)
                hour = random.randint(0, 23)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                
                """
                Generate the timestamp once we've generated all the numbers.
                Set the timezone to "UTC" to match the data.
                """
                
                timestamp = pd.Timestamp(year=year, month=month, day=day,
                                      hour=hour, minute=minute, second=second, tz="UTC")
                timestamp = timestamp.tz_localize(None)
                
                """
                STEP 2:
                Generate a fake magnitude.
                
                The magnitude scale is logarithmic, so to match this distribution, we
                will generate a random integer x = random.randint(0, 10**10).
                
                We will then calculate y = 10 - math.log(x, 10), which represents the magnitude.
                In other words, the more digits a number has, the lower its magnitude will be.
                Consequently, for every 10 earthquakes with magnitude ~0, we can expect 1
                earthquake with magnitude ~1.
                
                As such, we can approximate a logarithmic distribution.
                """
                
                x = random.randint(0, 10**10)
                y = 10 - math.log(x, 10)
                magnitude = int(y*100)/100
                
                """
                STEP 3:
                Generate random latitude, longitude, and depth numbers.
                
                The depth measurement is in kilometers (km). The maximum depth for
                an earthquake is estimated to be ~800 km as reported by the USGS
                (source in the README).
                
                Why are there division signs?
                The min and max bounds for latitude, longitude, and depth are multiplied
                by 100, while the result is divided by 100 so each measurement has two
                significant digits.
                """
                
                latitude = random.randint(-9000, 9000)/100
                longitude = random.randint(-18000, 18000)/100
                depth = random.randint(0, 80000)/100

                """
                STEP 4:
                Write down the data into the CSV!
                """
                row = [timestamp, magnitude, latitude, longitude, depth]
                rows.append(row)
            
            # If something went wrong, print out the error message.
            except Exception as e:
                print(str(e))
                
        """
        STEP 5:
        Write all the rows down.
        We'll sort all the rows by datetime ascending.
        """
        rows.sort(key=lambda x:x[0])
        csv_writer.writerows(rows)

# main method that calls the fake data generation function
if __name__ == "__main__":
    
    # set a random seed
    random.seed(12)
    
    # define the parameters
    NUM_EVENTS = 1000
    output_path = "src/fake_data/Fake Earthquakes (0-2023 AD).csv"
    
    # call the function
    create_fake_data(NUM_EVENTS, output_path)
