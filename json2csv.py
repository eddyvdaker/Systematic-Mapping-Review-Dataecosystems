"""
Convert json to csv
"""

import json
import csv

json_file = './results/results_5.json'
csv_file = './results/results.csv'

json_data = json.load(open(json_file))['results']
json_keys = json_data[0].keys()

lines = [json_keys]

for result in json_data:
    row = []
    for key in json_keys:
        row.append(result[key])
    lines.append(row)

with open(csv_file, 'w') as output:
    writer = csv.writer(output, delimiter='#')
    writer.writerows(lines)
