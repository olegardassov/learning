import re

with open('../people.txt', 'r', encoding='UTF8') as file:
    people_data = file.read()

    pattern = re.compile(r'^\b[A-Z][a-z]+\s\b[A-Z][a-z]+$', re.MULTILINE)
    matches = pattern.findall(people_data)
    for match in matches:
        print(match)


    pattern = re.compile(r'(^\d{1,5})+\s\w+\s(St\.,)\s[A-z][a-zA-Z\']+\s[A-Z]+\s\w+$', re.MULTILINE)
    matches = pattern.finditer(people_data) # with find all did not work, I don,t know why!
    for match in matches:
        print(match[0])
