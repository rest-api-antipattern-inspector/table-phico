import json


def get_json_data():
    with open("tables.json", "r") as read_file:
        return json.load(read_file)


def write_result_table(table):
    file = open("resultTables.json", "w")
    file.write(json.dumps(table))
    file.close()
