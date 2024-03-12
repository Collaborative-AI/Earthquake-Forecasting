from data_processor import DataProcessor

"""
Create DataProcessor objects for all the datasets used for the final dataset.
For more information on how DataProcessor is initialized, see data_processor.py
"""
argentina         = DataProcessor(datetime=[0], mag=1, lat=2, long=3, depth=4)
canada            = DataProcessor(datetime=[1], mag=6, mag_type=5, mag_letter="mw",
                                  lat=2, long=3, depth=4)
east_africa       = DataProcessor(datetime=[6], mag=1, lat=7, long=8, depth=9)
ghea              = DataProcessor(year=2, row=3, day=4, hour=5, minute=6, second=7,
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

