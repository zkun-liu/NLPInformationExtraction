import os
import pandas as pd
import csv
import itertools
import time

def improveCSV(directory): # Puts the CSV in proper format.
	# Group data by category
	for file in os.listdir(directory):
		newData = {}
		with open((directory + '/' + file), 'rt') as ogFile:
			csvReader = csv.reader(ogFile, delimiter=',', quotechar='"')
			for row in csvReader:
				if row[0] in newData:
					newData[row[0]].append(row[1])
				else:
					newData[row[0]] = [row[1]]

def main():
	nerOutputDir = r'NER-OUTPUT'
	print("Improving CSVs")
	improveCSV(nerOutputDir)
	print("****************************************")
	print("CSV improvement complete.")
	print("****************************************")
	print("")

main()