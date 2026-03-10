import json
import csv
# import openpyxl  #to work with excel files


#JSON Data Provider
def read_json_data(filepath):
    with open(filepath,"r") as f:
        data_list = json.load(f)
    return [(item,) for item in data_list]


#CSV Data Provider
def read_csv_data(filepath):
    data_list = []
    with open(filepath, "r") as f:
        reader = csv.reader(f) # Create a CSV reader object to read each row line by line in CSV
        next(reader)
        for row in reader:
            data_list.append(tuple(row))
    return data_list