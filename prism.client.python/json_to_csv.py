import json
import csv


def json_to_csv(json_file_path, csv_file_path, encoding='utf-8'):
    with open(json_file_path, 'r', encoding=encoding) as json_file:
        data = json.load(json_file)

    with open(csv_file_path, 'w+', newline='', encoding=encoding) as csv_file:
        writer = csv.writer(csv_file)
        # Write headers
        writer.writerow(data[0].keys())
        # Write data
        for row in data:
            writer.writerow(row.values())


def json_str_to_csv(json_str, csv_file_path, encoding='utf-8'):
    data = json.loads(json_str)
    with open(csv_file_path, 'w+', newline='', encoding=encoding) as csv_file:
        writer = csv.writer(csv_file)
        # Write headers
        writer.writerow(data[0].keys())
        # Write data
        for row in data:
            writer.writerow(row.values())
