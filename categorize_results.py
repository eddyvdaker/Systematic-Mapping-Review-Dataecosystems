"""
A script that shows the researcher the title and abstract of a source, then
gives the options to add an existing field or add a new field. These fields
are then saved. It is possible to stop in the middle and continue at the
same point afterwards.
"""

import json

new_results_file = './results/results_4.json'
old_results_file = './results/results_with_terms.json'
categories_file = './categories.json'

old_results = json.load(open(old_results_file))['with_terms']
nr_of_results = len(old_results)
new_results = json.load(open(new_results_file))['results']
categories = json.load(open(categories_file))['categories']

for i, result in enumerate(old_results):
    print(f'\n## Result {i}/{nr_of_results} ##')
    if result['title'] not in [x['title'] for x in new_results]:
        # Print Title & Abstract and show existing categories
        print(f'TITLE: {result["title"]}\n\n'
              f'ABSTRACT: {result["abstract"]}\n\n'
              f'select existing category, or create a new one:')

        print('[0]\t: Create New')
        for j, category in enumerate(categories):
            print(f'[{j + 1}]\t: {category}')

        # Ask and process user input
        while True:
            try:
                user_input = int(input('Input: '))
                if user_input == 0:
                    category = str(input('New category: '))
                    break
                elif user_input in range(1, len(categories) + 1):
                    category = categories[user_input - 1]
                    break
                else:
                    print('Invalid input, no category selected')
            except ValueError:
                print('Invalid input, must be an integer...')

        # Add category to dictionary
        result.update({'category': category})
        new_results.append(result)
        with open(new_results_file, 'w') as output:
            json.dump({'results': new_results},
                      output, sort_keys=True, indent=4)
        if category not in categories:
            categories.append(category)
            with open(categories_file, 'w') as output:
                json.dump({'categories': categories},
                          output, sort_keys=True, indent=4)
        print('Results saved...')
    else:
        print('result found in categorized results, moving on to next '
              'result...')
