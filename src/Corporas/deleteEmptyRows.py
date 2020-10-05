# Python program to delete empty rows

import csv

inputCSV = "testCorpora.csv"
outputCSV = "testCorporaNER2.csv"

with open(inputCSV) as in_file:
    with open(outputCSV, 'w') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if any(row):
                writer.writerow(row)