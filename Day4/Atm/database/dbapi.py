import json




def load_data_from_db(dbname):
    with open(dbname,'r') as f:
        return json.load(f)

def write_data_to_db(dbname,data):
    with open(dbname, "w+")as f:
        json.dump(data, f)