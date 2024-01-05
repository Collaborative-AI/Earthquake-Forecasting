# run on python 3.11.2
import datetime
import math

"""
find_stats function:
Find the min/max/average of column values in the earthquake dataset

Input:  input_path -> string filepath for input CSV file
Output: Printed output

"""
def find_stats(input_path: str, current_year: int):
    
    # verify the number of rows
    # starts at one since we don't count the header
    row_index = 1
    
    # store year, magnitude, and depth information in buckets
    year_buckets = [0 for i in range(current_year)]
    mag_buckets = [0 for i in range(10)]
    depth_buckets = [0 for i in range(10)]
    
    # find the min and max magnitude and depth
    minYear, maxYear = 2**10, -1
    minMag, maxMag = 2**10, -1
    minDepth, maxDepth = 2**10, -1
        
    with open(input_path, "r") as input_file:
        next(input_file, None)
        
        for line in input_file:
            
            # each line terminates with a "\n"
            # to process the data, remove the "\n" at the end of each line
            line = line[:-1]
            row = line.split(",")

            try:
                
                """
                STEP 1:
                Extract the year from each row, then record
                the earthquake's year into its respective bucket,
                along with the min/max year.
                """
                datetime = row[0]
                year = int(datetime[:4])
                year_buckets[year] += 1
                
                minYear = min(minYear, year)
                maxYear = max(maxYear, year)
                
                """
                STEP 2:
                Extract the magnitude from each row, then record
                the min/max/bucket data.
                """
                magnitude = float(row[1])
                
                """
                Buckets are grouped by integers. We'll assign buckets by flooring
                earthquake magnitudes. All negative magnitudes will be rounded to 0
                for simplicity.
                """
                modified_mag = max(0, int(magnitude))
                if 0 <= int(modified_mag) <= 9:
                    mag_buckets[modified_mag] += 1
                else:
                    print(f"Anomaly at row {row_index}: Magnitude is {depth}")
                
                # update the min/max magnitude
                minMag = min(minMag, magnitude)
                maxMag = max(maxMag, magnitude)
                
                """
                STEP 3:
                Extract the depth from each row, then record the min/max/bucket data.
                NOTE: Not ALL rows contain a depth value. In that case, ignore the row.
                """
                depth = float(row[4]) if len(row[4]) != 0 else None
                
                """
                Depth measurements will be grouped by intervals of 100km. According to the
                USGS, the deepest earthquakes happen at roughly ~800 km, so anything deeper
                will print a message to call ourattention.
                """
                if depth != None:
                    modified_depth = max(0, int(depth/100))
                    if 0 <= modified_depth <= 9:
                        depth_buckets[modified_depth] += 1
                    else:
                        print(f"Anomaly at row {row_index}: Depth is {depth} km")
                        
                    minDepth = min(minDepth, depth)
                    maxDepth = max(maxDepth, depth)
            
                """
                STEP 4:
                Update the row index counter prior to moving on.
                """
                row_index += 1
                
            # print any exception at any rows
            except Exception as e:
                msg = f"At row {row_index}: {str(e)}"
                print(msg)
    
    """
    STEP 5:
    Print the number of rows in the dataset as a double-check.
    """
    msg = f"\nThere are {row_index} rows in the dataset."
    print(msg, "\n")
    
    """
    STEP 6:
    Print the #quakes by century
    
    Calculate a running sum over the buckets and print at the end
    of every century (or up to the present year)
    """
    num_centuries = math.ceil(len(year_buckets)/100)
    for k in range(num_centuries):
        lo, hi = k*100, min(current_year, (k+1)*100)
        summ = sum(year_buckets[lo:hi])
        msg = f"#Quakes from years [{lo}, {hi}): {summ}"
        print(msg)
    print()
    
    """
    STEP 7:
    Print the #quakes by magnitude
    """
    for k in range(len(mag_buckets)):
        msg = f"#Quakes with magnitude [{k}, {k+1}): {mag_buckets[k]}"
        print(msg)
    print()
        
    """
    STEP 8:
    Print the #quakes by depth by increments of 100km
    """
    for k in range(len(depth_buckets)):
        msg = f"#Quakes at depth [{k*100}, {(k+1)*100}) km: {depth_buckets[k]}"
        print(msg)
    
    
# main method that calls the fake data generation function
if __name__ == "__main__":
    
    # define the parameters then call the function
    input_path = "src/fake_data/Completed-Merge.csv"
    find_stats(input_path, datetime.datetime.today().year)

"""
OUTPUT:

There are 8034495 rows in the dataset. 

#Quakes from years [0, 100): 1
#Quakes from years [100, 200): 10
#Quakes from years [200, 300): 3
#Quakes from years [300, 400): 7
#Quakes from years [400, 500): 4
#Quakes from years [500, 600): 12
#Quakes from years [600, 700): 3
#Quakes from years [700, 800): 18
#Quakes from years [800, 900): 25
#Quakes from years [900, 1000): 12
#Quakes from years [1000, 1100): 27
#Quakes from years [1100, 1200): 27
#Quakes from years [1200, 1300): 41
#Quakes from years [1300, 1400): 46
#Quakes from years [1400, 1500): 57
#Quakes from years [1500, 1600): 114
#Quakes from years [1600, 1700): 272
#Quakes from years [1700, 1800): 311
#Quakes from years [1800, 1900): 1381
#Quakes from years [1900, 2000): 1446745
#Quakes from years [2000, 2024): 6590107

#Quakes with magnitude [0, 1): 1897634
#Quakes with magnitude [1, 2): 2584093
#Quakes with magnitude [2, 3): 1786763
#Quakes with magnitude [3, 4): 1069766
#Quakes with magnitude [4, 5): 583693
#Quakes with magnitude [5, 6): 96184
#Quakes with magnitude [6, 7): 12474
#Quakes with magnitude [7, 8): 3463
#Quakes with magnitude [8, 9): 432
#Quakes with magnitude [9, 10): 12

#Quakes at depth [0, 100) km: 7560589
#Quakes at depth [100, 200) km: 315396
#Quakes at depth [200, 300) km: 52813
#Quakes at depth [300, 400) km: 18335
#Quakes at depth [400, 500) km: 13556
#Quakes at depth [500, 600) km: 22129
#Quakes at depth [600, 700) km: 8710
#Quakes at depth [700, 800) km: 458
#Quakes at depth [800, 900) km: 5
#Quakes at depth [900, 1000) km: 0

"""