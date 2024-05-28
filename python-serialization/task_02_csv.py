#!/usr/bin/python3
""" function that creates an Object from a “CSV file”"""

import csv
import json


def convert_csv_to_json(csv_filename):
    with open(csv_filename, encoding='utf-8') as csv_file:
        dictcsv = csv.DictReader(csv_file)
        data = [row for row in dictcsv]

    with open('data.json', mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
