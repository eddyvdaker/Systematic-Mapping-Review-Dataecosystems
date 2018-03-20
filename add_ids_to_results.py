"""
A simple script that adds an ID field to each of the results.
"""

import json

print('Reading data...')
file = './results/results_4.json'
data = json.load(open(file))['results']

new_file = './results/results_5.json'
new_results = []

print('Iterating over results and adding ID...')
for i, result in enumerate(data):
    print(result)
    result.update({'id': i})
    new_results.append(result)

print('Writing new results to file...')
with open(new_file, 'w') as output:
    json.dump({'results': new_results},
              output, sort_keys=True, indent=4)
print('Done...')
