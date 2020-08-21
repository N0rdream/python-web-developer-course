import json
import csv


def create_csv(data):
    with open('output.csv', 'w') as f:
        w = csv.writer(f)
        w.writerows(data.items())

def create_json(data):
    with open('output.json', 'w') as f:
        json.dump(data, f)