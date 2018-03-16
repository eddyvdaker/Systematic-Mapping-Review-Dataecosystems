"""
This script parses the xml files, extracts the relevant fields and writes
the results to json and csv (for easy import into spreadsheets) files.
"""

import bs4
import json


def read_files(files):
    xml = ""
    for i, file in enumerate(files):
        with open(file) as df:
            xml += f'<q{i}>\n{df.read()}</q{i}>\n'

    return xml


def get_authors(parser):
    authors_list = [str(x)[4:-5] for x in parser.findAll('au')]
    authors_cleaned = ""
    for author in authors_list:
        authors_cleaned += f'; {author}'
    return authors_cleaned[2:]


def get_publish_date(parser):
    publish_date = parser.find('dt')
    return f'{publish_date["year"]}-{publish_date["month"]}-{publish_date["day"]}'


test_files = ['./results/single-result.xml', './results/single-result.xml']
result_files = ['./results/q1-results.xml', './results/q2-results.xml', './results/q3-results.xml']
files = result_files

print('Reading original files...')
xml = read_files(files)

print('Setting up parser...')
parser = bs4.BeautifulSoup(xml, 'lxml')
entries = []
rec_nr = 0

print('Start parsing entries...')
for i in range(len(files)):
    query = str(parser.find(f'q{i}'))
    query_parser = bs4.BeautifulSoup(query, 'lxml')

    records = [str(x) for x in query_parser.findAll('rec')]
    for record in records:
        rec_nr += 1
        print(f'currently at record {rec_nr}')
        rec_parser = bs4.BeautifulSoup(record, 'lxml')

        title = str(rec_parser.find('atl'))[5:-6]
        authors = get_authors(rec_parser)
        publish_date = get_publish_date(rec_parser)
        publication_type = str(rec_parser.find('pubtype'))[9:-10]
        database = str(rec_parser.find('header')['longdbname'])
        url = str(rec_parser.find('url'))[5:-6]
        language = str(rec_parser.find('language'))[21:-11]
        journal = str(rec_parser.find('jtl'))[5:-6]
        abstract = str(rec_parser.find('ab'))[4:-5]

        entries.append({
            'title': title,
            'authors': authors,
            'publish_date': publish_date,
            'publication_type': publication_type,
            'database': database,
            'url': url,
            'language': language,
            'journal': journal,
            'abstract': abstract
        })

print('writing json results...')
with open('./results/results.json', 'w') as output:
    json.dump({'results': entries}, output, sort_keys=True, indent=4)
