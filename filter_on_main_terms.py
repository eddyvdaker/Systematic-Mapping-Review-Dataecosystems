"""
A script that scans the results for titles and abstracts containing the main
search terms and placing them in a seperate file. The results that do not
contain the search terms are also saved in a different file, for later
analysis.
"""

import json

print('reading data...')
file = './results/results_2.json'
results = json.load(open(file))['results']

terms = ['data ecosystem', 'open data ecosystem', 'big data ecosystem']
results_with_terms = []
nr_results_with_terms = 0
results_without_terms = []
nr_results_without_terms = 0

print('start checking results...')
for result in results:
    if any(term in result['title'].lower() for term in terms):
        results_with_terms.append(result)
        nr_results_with_terms += 1
    elif any(term in result['abstract'].lower() for term in terms):
        results_with_terms.append(result)
        nr_results_with_terms += 1
    else:
        results_without_terms.append(result)
        nr_results_without_terms += 1
    print(f'{nr_results_with_terms + nr_results_without_terms} checked...')

print('writing results to file...')
with open('./results/results_with_terms.json', 'w') as output:
    json.dump({'with_terms': results_with_terms},
              output, sort_keys=True, indent=4)

with open('./results/results_without_terms.json', 'w') as output:
    json.dump({'without_terms': results_without_terms},
              output, sort_keys=True, indent=4)

print('done...')
print(f'found {nr_results_with_terms} with the search terms, and '
      f'{nr_results_without_terms} without...')
