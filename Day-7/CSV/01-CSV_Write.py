import csv

data = [
    "firstname, lastname",
    "sachin,tendulkar",
    "virat,kohli",
    "ms,dhoni",
    "yuvraj,singh"
]

# file = open('data.csv','w')
# file.close
with open('data.csv', 'w', newline='') as file:
    # writer = csv.writer(file, delimiter='|')
    writer = csv.writer(file)

    for d in data:
        writer.writerow(d.split(","))