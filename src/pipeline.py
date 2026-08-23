import csv,json
class DataPipeline:
    def __init__(self,config_path):
        with open("config.json","r",newline="",encoding="utf-8") as config_fle:
            config = json.load(config_fle)
            self.source=config["source"]
            self.destination=config["destination"]
    # EXTRACT DATA
    def extract_data(self):
        print(f"Extracting data...{self.source}")
        data=[]
        with open(self.source,newline="",encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data
    # CLEAN DATA
    def clean_data(self,data):
        print(f"Cleaning data...{self.source}")
        cleaned = []
        for row in data:
            if row["amount"] not in [None,"","NULL"]:
                row["amount"] = float(row["amount"])
                cleaned.append(row)
        return cleaned
    # LOAD DATA
    def load_data(self,data):
        print(f"Loading data...{len(data)} to {self.destination}")
        if not data:
            print("No data to load")
            return
        print(data)
        with open(self.destination,"w",newline="",encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    #ORCHESTRATION
    def run(self):
        data= self.extract_data()
        data = self.clean_data(data)
        self.load_data(data)
        # OR
        # self.load_data(self.clean_data(self.extract_data()))
D1=DataPipeline("config.json")
D1.run()






