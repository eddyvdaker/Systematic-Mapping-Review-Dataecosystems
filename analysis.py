"""
A script that extracts some numbers from the data found thus far.
"""

import json

data_file = './results/results_5.json'
data = json.load(open(data_file))['results']

categories_file = './categories.json'
categories = json.load(open(categories_file))['categories']

summary_file = './results/summary.json'

# Count the number of results for each of the categories
occurrences_per_category = {}
for category in categories:
    occurrences = 0
    for result in data:
        if result['category'] == category:
            occurrences += 1
    occurrences_per_category.update({category: occurrences})

# Find any systematic (mapping/literature) reviews
systematic_reviews = []
terms = ['systematic review', 'systematic mapping review',
         'systematic literature review']
for result in data:
    if any(term in result['abstract'].lower() for term in terms):
        systematic_reviews.append(result['id'])

# Find number of conference publications and articles
result_types = {'conference': 0, 'journal': 0, 'other': 0}
for result in data:
    if 'conference' in result['publication_type'].lower():
        result_types['conference'] += 1
    elif 'journal' in result['publication_type'].lower():
        result_types['journal'] += 1
    else:
        result_types['other'] += 1

# Find the number of occurrences of each of the search terms
search_terms = {'big data ecosystem': 0,
                'open data ecosystem': 0,
                'data ecosystem': 0}

for result in data:
    text = f'TITLE: {result["title"]} ABSTRACT: {result["abstract"]}'
    count_big_data_ecosystem = text.lower().count('big data ecosystem')
    count_open_data_ecosystem = text.lower().count('open data ecosystem')
    count_data_ecosystem = text.lower().count('data ecosystem')

    search_terms['big data ecosystem'] += count_big_data_ecosystem
    search_terms['open data ecosystem'] += count_open_data_ecosystem
    search_terms['data ecosystem'] += count_data_ecosystem \
                                      - count_big_data_ecosystem \
                                      - count_open_data_ecosystem

with open(summary_file, 'w') as output:
    results = {}
    results.update({'occurrences per category': occurrences_per_category})
    results.update({'systematic reviews': systematic_reviews})
    results.update({'result types': result_types})
    results.update({'search terms': search_terms})

    json.dump(results, output, sort_keys=True, indent=4)
