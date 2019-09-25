import json

def load_data():
    with open("data.json") as f:
        data = json.load(f)
        return data


data = load_data()
