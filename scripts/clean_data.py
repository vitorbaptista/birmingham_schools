import os
import csv
import tempfile

path = os.path.join(
    os.path.dirname(__file__),
    '../data/birmingham_schools.csv'
)

def clean_data(path):
    with open(path) as inp, tempfile.NamedTemporaryFile('w', delete=False) as output:
        # Lowercase all headers
        headers = inp.readline().strip().lower().split(',')

        reader = csv.DictReader(inp, fieldnames=headers)
        writer = csv.DictWriter(output, fieldnames=headers)
        writer.writeheader()

        for row in reader:
            row = fix_kingsland_url(row)
            writer.writerow(row)

    os.replace(output.name, path)


def fix_kingsland_url(row):
    if row['web_site'] == 'www.kingsland.bham.sch.uk/':
        row['web_site'] = 'http://{}'.format(row['web_site'])
    return row


if __name__ == '__main__':
    clean_data(path)
