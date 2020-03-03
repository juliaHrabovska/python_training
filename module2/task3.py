import csv
import json

csv_rows = []
with open('utils_cars.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    title = reader.fieldnames
    for row in reader:
        csv_rows.extend([{title[i]: row[title[i]] for i in range(len(title))}])
with open('result.json', 'w') as json_file:
    json.dump(csv_rows, json_file, indent=2)
