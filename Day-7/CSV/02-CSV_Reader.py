import csv

with open('data.csv') as file:
    reader = csv.reader(file)

    for data in reader:
        print(data)