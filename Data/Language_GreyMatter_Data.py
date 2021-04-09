import csv

dict_list = list()
with open("/Users/parkerhicks/Desktop/Biostats_data/chap16q15LanguageGreyMatter.csv") as f:
    records = csv.DictReader(f)
    for row in records:
        dict_list.append(row)
    print(dict_list)

example = dict_list[0]
print(example)


