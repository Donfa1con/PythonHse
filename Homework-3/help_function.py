import json

def record_to_file(data, file_name):
    with open(file_name, "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii = False)

def read_the_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)
