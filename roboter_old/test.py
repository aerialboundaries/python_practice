# -*- coding: utf-8 -*-



import csv
with open('test.csv', 'w+', newline='') as csv_1:
    writer = csv.DictWriter(csv_1, ['C1', 'C2'])
    writer.writeheader()
    