"""
This script parses the xml files, extracts the relevant fields and writes
the results to json and csv (for easy import into spreadsheets) files.
"""

import bs4


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


heading = ['id', 'query', 'in_query_id', 'title', 'author', 'publish_date', 'journal', 'publisher',
           'article_or_conference-proceding', 'database', 'url', 'language',
           'abstract']
test_files = ['./results/single-result.xml', './results/single-result.xml']
result_files = ['./results/q1-results.xml', './results/q2-results.xml', './results/q3-results.xml']
files = test_files


xml = read_files(files)
parser = bs4.BeautifulSoup(xml, 'lxml')
id = 0
json_results = {}

for i in range(len(files)):
    query = str(parser.find(f'q{i}'))
    query_parser = bs4.BeautifulSoup(query, 'lxml')

    records = [str(x) for x in query_parser.findAll('rec')]
    for record in records:
        rec_parser = bs4.BeautifulSoup(record, 'lxml')

        title = str(rec_parser.find('atl'))[5:-6]
        authors = get_authors(rec_parser)
        publish_date = get_publish_date(rec_parser)
        publication_type = str(rec_parser.find('pubtype'))[9:-10]
        database = str(rec_parser.find('header')['longdbname'])
        url = str(rec_parser.find('url'))[5:-6]
        language = str(rec_parser.find('language'))[21:-11]
        abstract = str(rec_parser.find('ab'))[4:-5]
        journal = str(rec_parser.find('jtl'))[5:-6]
        


