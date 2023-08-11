import csv
from datetime import datetime


def openCSV(fileName):
    with open(f'data\\csv\\{fileName}.csv', encoding='utf-8') as input:
        csv_reader = csv.DictReader(input, delimiter=',')

        list = [row for row in csv_reader]

        return list
