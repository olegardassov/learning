###Roman

import csv

data_list = []
with open("../2019.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",", lineterminator="\n")
    next(csv_file)
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        data_list.append(line)

print(data_list)

result_list = []
top_list = []
for x in data_list:
    top_list.append(x["GDP per capita"])
while len(result_list) < 10:
    for x in data_list:
        if x["GDP per capita"] == max(top_list) and x not in result_list:
            result_list.append(x)
            top_list.remove(x["GDP per capita"])

for res in result_list:
    print(res)




