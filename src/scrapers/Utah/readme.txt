#-------------------------------------------------------------------------------
detections.txt

A catalog with newly detected earthquakes for the Mineral Mountains
Time period: 2016/09-2019/12
Number of detectons : 1,100

#Column 01: Year
#Column 02: Origin Time (UTC) [Month-day-hour-min-sec]
#Column 03: Latitude (degrees N)
#Column 04: Longitude (degrees W)
#Column 05: Depth (km) [from surface]
#Column 06: Template event Maginute [Ml/Mc]
#Column 07: Detection Magnitude
#Column 08: ID for event template 
#Column 09: ID for detection
#Column 10: Correlation Coefficient

#------------------------------------------------------------------------------- 
relocated.txt

A relocated catalog for the Mineral Mountains combining originally
cataloged earthquakes and new detections

Time period: 2016/09-2019/12
Number of events: 802

#Column 01: Year
#Column 02: Origin Time (UTC) [Month-day-hour-min-sec]
#Column 03: Latitude (degrees N)
#Column 04: Longitude (degrees W)
#Column 05: Depth (km) [from surface]
#Column 06: Magnitude
#Column 07: Event ID [ Note: 1-75 correspond to originally catalog earthquakes] 

#-------------------------------------------------------------------------------
multiplets.txt

Families of repeating events in the Mineral Mountains

Column 01: year
Column 02: month
Column 03: day
Column 04: hour 
Column 05: min
Column 06: sec
Column 07: latitude (degrees N)
Column 08: longitude (degrees W)
Column 09: depth (km) [from surface]
Column 10: magnitude
Column 11: Event ID
Column 12: Multiplet ID
Column 13: N of events in the multiplet
Column 14: [1] for phase-pick and CC relocation, [0] for phase-pick relocation
