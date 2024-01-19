README file for GHEAScraper.py

Summary:
Converts a TXT file from the GHEA (Global Historical Earthquake Archive) into a CSV file.
The data can be found at: http://evrrss.eri.u-tokyo.ac.jp/db/ghec/index.html

Finding the TXT file:
- Locate the bullet point "the Global Historical Earthquake Catalogue - GHEC v1.0"
- Click "download GHEC v1.0 as text (ASCII) file"

Header Information (sourced from website):
# CODE	DESCRPTION	NOTES
# En	Event number	unique ID of the catalogue, in chronological order
# Source	Main source	selected dataset for time, epicentral coordinates, depth, Io
# Year	Origin time: year	from the selected dataset
# Mo	Origin time: month	from the selected dataset
# Da	Origin time: day	from the selected dataset
# Ho	Origin time: hour	from the selected dataset
# Mi	Origin time: minutes	from the selected dataset
# Se	Origin time: seconds	from the selected dataset
# Area	Epicentral area	from the selected dataset, or (in square brackets) the country (as of today) where the epicentre is located
# Lat	Epicentral latitude	from the selected dataset
# Lon	Epicentral longitude	from the selected dataset
# LatUnc	Uncertainty of epicentral latitude	in km, from the selected dataset, when available
# LonUnc	Uncertainty of epicentral longitude	in km, from the selected dataset, when available
# EpDet	Type of epicentre determination	bx: determined according to the method by Gasperini et al. (1999; 2010)
# 		bw: determined according to the method by Bakun and Wenthworth (1997)
# 	 	cat: derived from another catalogue
# 	 	instr: instrumental
# Dep	depth	in km
# Io	epicentral intensity	from the selected dataset
# Msource	source for the magnitude	the same as "Source", with 65 exceptions
# M	magnitude	from Msource
# MUnc	magnitude uncertainty	from Msource, when available
# MType	type of magnitude	w: Mw
# 	 	s: Ms
# 	 	jma: Mjma
# 	 	<blank>: not specified by the source
# MDet	Type of magnitude determination	bx: determined according to the method by Gasperini et al. (1999; 2010)
# 	 	bw: determined according to the method by Bakun and Wenthworth (1997)
# 	 	int: converted from epicentral or maximum intensity
# 	 	cat: derived from another catalogue
# 	 	instr: instrumental
# MDPsource	Source of the Macroseismic Data Points	 
# MDPn	Number of Macroseismic Data Points	 
# MDPIx	Maximum intensity	 
# MDPsc	Macroseimic scale of the MPDs	MM: modified Mercalli
# 		MSK: Medvedev-Sponheuer-Karnik
# 		EMS: European Macroseimic Scale
# 		MCS: Mercalli-Cancani-Sieberg
# 		JMA: Japan Meteorological Agency
# Remarks	 Additional information from the source

The following lines can be modified:
Line 25:        Modify the file path of the input .txt file
Line 26:        Modify the file path of the output .csv file
