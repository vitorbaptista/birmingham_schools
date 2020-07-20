import os
import csv
import tempfile


DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    '../data/birmingham_schools.csv'
)


def clean_data(path):
    with open(path) as inp, \
         tempfile.NamedTemporaryFile('w', delete=False) as output:
        # Lowercase all headers
        headers = [
            # Rename _geom to geom, as the Data Store fails
            # on loading headers starting with underscore
            header.lstrip('_')
            for header in inp.readline().strip().lower().split(',')
        ]

        reader = csv.DictReader(inp, fieldnames=headers)
        writer = csv.DictWriter(output, fieldnames=headers)
        writer.writeheader()

        for row in reader:
            row = fix_urls(row)
            writer.writerow(row)

    os.replace(output.name, path)


def fix_urls(row):
    fixed_url_mapping = {
        'www.kingsland.bham.sch.uk/': 'http://www.kingsland.bham.sch.uk/',
        'http://www.watrmill.bham.sch.uk/': 'http://www.watermill.bham.sch.uk/',
    }
    if row['web_site'] in fixed_url_mapping:
        row['web_site'] = fixed_url_mapping[row['web_site']]
    return row


if __name__ == '__main__':
    clean_data(DATA_PATH)
