import json
import csv

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

with open('output.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Write headers
    writer.writerow(data[0].keys())
    # Write data
    for row in data:
        writer.writerow(row.values())
