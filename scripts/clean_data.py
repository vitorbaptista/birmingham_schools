import os
import tempfile

path = os.path.join(
    os.path.dirname(__file__),
    '../data/birmingham_schools.csv'
)


with open(path, 'rb') as inp, tempfile.NamedTemporaryFile(delete=False) as output:
    for row in inp:
        modified_row = row.replace(
            b'www.kingsland.bham.sch.uk/',
            b'http://www.kingsland.bham.sch.uk/'
        )
        output.write(modified_row)


os.replace(output.name, path)
