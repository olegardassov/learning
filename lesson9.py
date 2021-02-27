# word_list = ["Hello", "people", "you", "how", "are", "people", "are"]
#
# print(len(word_list))
# print(len(set(word_list)))
#
# unique = []
# for word in word_list:
#     if word not in unique:
#         unique.append(word)
# print(len(unique))
#
# with open('homework.txt', "w" , encoding="UTF8") as file:
#     file.write("There are " + str(len(word_list)) + " words in text file.\n")
#     file.write("There are" + str(len(set(word_list))) + " unique words in text file.")


#_________________________JSON format .json
# IN JSON file true and false is written with lower case and none = null
# import json
# json_string = '''
# {
#   "people": [
#     {
#       "name": "Jack Sumers",
#       "phone": "555-555-555",
#       "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
#       "has_licence": false
#     },
#     {
#       "name": "Mary Smith",
#       "phone": "777-777-777",
#       "emails": null,
#       "has_licence": true
#     }
#   ]
# }'''
#
# data = json.loads(json_string)

# print(type(data))
# print(data)
#
# print(type(data["people"]))
# print(data["people"])   # we can return all included in "people"

#_________________________

# for person in data["people"]:
#     print(person["emails"]) #will return value of emails
#     # print(person["emails"][0])  # will return value of emails
#
# people = data["people"][1] # will choose second name (first is index 0)
# print(people["name"]), people["phone"]
#print(people)

#_______DELETE

# for person in data["people"]:
#     del person["phone"]
#     print(person)

#_______________ Method dumps is used to save to file
# print(type(data))
# print(data)
# new_string = json.dumps(data, indent=2, sort_keys=True) #sort_keys will sort keys in alphabetical order
# print(new_string)
# print(type(new_string))
#
# people = data["people"]
# person = people[0]
# print(person["name"])
# print(person["emails"])
# print(person["phone"])


#_____________________ New Sample
#loads = work with str
#load = work with file
# import json
#
# with open("sample2.json", "r" , encoding="UTF8") as file:
#     #Method "load" is user to read a file and "loads" is used to read string
#     data = json.load(file)
#     print(data)
#
# # for loop to delete person["has_licence"] entry if it is equal to False
# for person in data["people"]:
#     if person["has_licence"] == False:
#         del person["has_licence"]   # if person does not have the licence this line will be deleted
#
# with open("sample_edited.json", "w") as file:  # creates new file in that file ho did not have licence, the line will be deleted
#     json.dump(data, file, indent=2)


#___________________CSV
# import csv
#
# with open("test.csv", "r", encoding="UTF8") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     print(csv_reader)
#
#     next(csv_reader)  # skips first line in our table
#
#     for line in csv_reader:  # to return as list in table
#         print(line) # returns whole table
#         print(line[2]) # returns only each third title from table index works from 0

#_______________________________New Sample
import csv

with open("test.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("test_copy.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter=",", lineterminator="\n")

        for line in csv_reader:
            csv_writer.writerow(line)


#make program using 3 scores which country is better, higher the score better it is . return top10 countries using some score




