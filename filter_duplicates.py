"""
A script that checks the output json file and removes duplicates
"""
import json

file = './results/results.json'

print('reading json from file...')
results = json.load(open(file))['results']
new_results = []
duplicates = 0

print('checking for duplicates...')
for i, result in enumerate(results):
    if result not in new_results:
        new_results.append(result)
    else:
        duplicates += 1
    print(f'{i + 1} results checked...')

print('writing new results to file...')
with open('./results/results_2.json', 'w') as output:
    json.dump({'results': new_results}, output, sort_keys=True, indent=4)

print('done...')
print(f'removed {duplicates} duplicates from a total off {len(results)} results...')
