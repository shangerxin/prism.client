
import csv
import json


def csv_to_json(csv_file_path, json_file_path, encoding='utf-8'):
    # Read CSV and add to a list
    data = []
    with open(csv_file_path, encoding=encoding) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    # Write to JSON file
    with open(json_file_path, 'w+', encoding=encoding) as json_file:
        json_file.write(json.dumps(data, indent=4))

def csv_to_json_str(csv_file_path, encoding='utf-8'):
    # Read CSV and add to a list
    data = []
    with open(csv_file_path, encoding=encoding) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return json.dumps(data, indent=4)


def csv_to_json_obj(csv_file_path, encoding='utf-8'):
    # Read CSV and add to a list
    data = []
    with open(csv_file_path, encoding=encoding) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    return data


def csv_to_json_one_line_str(csv_file_path, encoding='utf-8'):
    # Read CSV and add to a list
    data = []
    with open(csv_file_path, encoding=encoding) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return json.dumps(data)