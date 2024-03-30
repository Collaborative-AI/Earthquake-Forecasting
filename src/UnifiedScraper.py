class UnifiedScraper:
    def __init__(self):
        self.scrapers = [
            {"input_path": "src/scraper/Argentina/raw/clean-catalog.xml", "output_path": "src/scraper/Argentina/clean/Argentina Andean Earthquakes (2016-2017).csv", "data_type": "xml", "header": ["Time ID", "Magnitude", "Latitude", "Longitude", "Depth"]},
            {"input_path": "src/scraper/Canada/raw/Canada-19850109-20240119.txt", "output_path": "src/scraper/Canada/clean/Canada (1985-2024).csv", "data_type": "txt", "header": ["Time ID", "Magnitude", "Latitude", "Longitude", "Depth"], "separator": "|", "num_skips": 0},
            {"input_path": "src/scraper/World_Tremor/japan", "output_path": "src/scraper/World_Tremor/clean/Japan Database (2005-2014).csv", "data_type": "txt", "num_skips": 0},
            {"input_path": "src/scraper/GHEA/raw/GHEA-data.txt", "output_path": "src/scraper/GHEA/clean/GHEA (1000-1903).csv", "data_type": "txt", "separator": "\t", "num_skips": 78},
            {"input_path": "src/scraper/NOAA/raw/NCEI-WDS-Earthquakes.tsv", "output_path": "src/scraper/NOAA/clean/NOAA NCEI-WDS (0-2023).csv", "data_type": "txt", "separator": "\t", "num_skips": 0},
            {"input_path": "src/scraper/SoCal/raw/SearchResults.txt", "output_path": "src/scraper/SoCal/clean/SCEDC (1932-2023).csv", "data_type": "txt", "num_skips": 2},
            {"input_path": "src/scraper/Turkey/raw/turkey_earthquakes(1915-2021).csv", "output_path": "src/scraper/Turkey/clean/Turkey (1915-2021).csv", "data_type": "csv", "separator": ";", "num_skips": 0},
            {"input_path": "src/scraper/World_Tremor/global", "output_path": "src/scraper/World_Tremor/clean/World Tremor Database (2005-2014).csv", "data_type": "txt", "num_skips": 0}
        ]


    def add_scraper(self, input_path, output_path, data_type, header=None, separator=",", num_skips=0):
        """
        Adds a new scraper configuration.
        """
        config = {
            "input_path": input_path,
            "output_path": output_path,
            "data_type": data_type,
            "header": header,
            "separator": separator,
            "num_skips": num_skips
        }
        self.scrapers.append(config)

    def find_quakes(self):
        for config in self.scrapers:
            if config["data_type"] == "xml":
                self.process_xml(config)
            elif config["data_type"] in ["txt", "tsv", "csv"]:
                self.process_text(config)

    def process_xml(self, config):
        tree = ET.parse(config["input_path"])
        root = tree.getroot()

        with open(config["output_path"], 'w', newline='') as file:
            csv_writer = writer(file)
            if config.get("header"):
                csv_writer.writerow(config["header"])

            for quake in root.findall(".//earthquake"):
                time_id = quake.find('time').text
                magnitude = quake.find('magnitude').text
                latitude = quake.find('latitude').text
                longitude = quake.find('longitude').text
                depth = quake.find('depth').text
                csv_writer.writerow([time_id, magnitude, latitude, longitude, depth])

    def process_text(self, config):
        with open(config["input_path"], 'r') as file:
            lines = file.readlines()[config["num_skips"]:]

        with open(config["output_path"], 'w', newline='') as file:
            csv_writer = writer(file)
            if config.get("header"):
                csv_writer.writerow(config["header"])

            for line in lines:
                row = line.strip().split(config.get("separator", ","))
                csv_writer.writerow(row)

if __name__ == "__main__":
    scraper = UnifiedScraper()
    # Additional scraper configurations can be added dynamically using scraper.add_scraper(...)
    scraper.find_quakes()