import re

#____EXCERCISE 1

rgb_colors = '''
#b4efab
#d3efab
#eaabef
hello
#howareyou
#hello1
#efe8ab
#efabb5
#efabab
#000
'''

pattern = re.compile(r'#[0-9a-fA-F]{3,6}') # I could use #[1-9a-f]+, but in that case if word would be over 6 symbols containing [1-9a-f] it would return it as well!
# pattern = re.compile(r'#[0-9a-fA-F]{3,6}') #Romans variant.
matches = pattern.finditer(rgb_colors)
for match in matches:
    print(match[0])

#____EXCERCISE 2

example = '''
2*9-6*5
(3+5)-9*4
'''
pattern = re.compile(r'[0-9][^+]')
# pattern = re.compile(r'\d+[^+]') #Romans variant
# pattern = re.compile(r'[^\d+][\d]')
matches = pattern.finditer(example)
for match in matches:
    print(match[0])
    print(match.group()[0:-1]) # returns only value


#____EXCERCISE 3

time = '''
Завтрак в 09:00
11:15
23:59
12:12
01:59
17:39
37:98
210:124
23:248' 
'''
pattern = re.compile(r'[0-2][0-9]:[0-6][0-9]')
# pattern = re.compile(r'\b([0-1][0-9]|2[0-3]):[0-5][0-9][^0-9]') #Romnans variant
matches = pattern.findall(time)
for match in matches:
    print(match)
    print(match.group[0:-1])    # Romans


#____EXCERCISE 5

string = '''
hello I am oleg
Hello, my name is Oleg and I am 30 years old!
Today is+good weather_!
'''
pattern = re.compile(r'[^a-zA-Z0-9]')   # Romans version
matches = pattern.findall(string)
if len(matches) != 0:
    print("OK")
else:
    print("NOK")


pattern = re.compile(r'\w+')
matches = pattern.findall(string)
for match in matches:
    print(match)

#____EXCERCISE 6

isikukood = '''
Minu isikukood on 39005110299!
'''

# pattern = re.compile(r'^[34]\d{10}$', re.MULTILINE)
pattern = re.compile(r'\b[34]\d{2}[01][0-9][0-3][0-9]\d{4}')
pattern = re.compile(r'\b[3456][0-9]{2}(0[0-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])\d{4}')    #Romans version
# pattern = re.compile(r'^[34]\d{10}$') #why does not work like that?
matches = pattern.findall(isikukood)
for match in matches:
    print(match)