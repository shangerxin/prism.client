
import csv
import json

csv_file_path = 'data.csv'
json_file_path = 'data.json'

# Read CSV and add to a list
data = []
with open(csv_file_path, encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# Write to JSON file
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json.dumps(data, indent=4))
