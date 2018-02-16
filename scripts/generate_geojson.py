import os
import csv
import json

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    '../data/birmingham_schools.csv'
)


OUTPUT_PATH = os.path.join(
    os.path.dirname(__file__),
    '../data/birmingham_schools.geojson'
)


def generate_geojson(path, output_path):
    geojson = {
        'type': 'FeatureCollection',
        'features': [],
    }
    with open(path) as csvfile:
        for row in csv.DictReader(csvfile):
            feature = {
                'type': 'Feature',
                'geometry': json.loads(row['_geom']),
                'properties': row,
            }
            del feature['properties']['_geom']
            geojson['features'].append(feature)

    with open(output_path, 'w') as geojsonfile:
        json.dump(geojson, geojsonfile, indent=2)


if __name__ == '__main__':
    generate_geojson(DATA_PATH, OUTPUT_PATH)
