# Code origin: https://www.geeksforgeeks.org/convert-csv-to-json-using-python/
# Modified by: Mingyang Li 

import csv
import json

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data

        # Initialise unique primary key
        primaryKey = 1
        for row in csvReader:
            # convert amount value into integer inplace
            row["Amount (NZD)"] = float(row["Amount (NZD)"])
            data[primaryKey] = row

            primaryKey += 1
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
         
# Driver Code
 
# Decide the two file paths according to your
# computer system
csvFilePath = r'expenses.csv' # or income.csv
jsonFilePath = r'expenses.json' # or income.json that's empty
 
# Call the make_json function
make_json(csvFilePath, jsonFilePath)