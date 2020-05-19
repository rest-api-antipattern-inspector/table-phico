import json


def get_json_data():
    with open("tables.json", "r") as read_file:
        return json.load(read_file)
