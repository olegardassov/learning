# import re
#
# text_to_search = '''
# abcdefghijklmnopqurtuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa HaHaHa
# MetaCharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )
# example.com
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 800-555-1234
# 900-555-1234
# Mr. Jones
# Mr Smith
# Ms Davis
# Mrs. Robinson
# Mr. T
# Mr. JONES
# abc
# hall mall wall ball
# '''
#
# sentence = 'Start a sentence and then bring it to an end'

# print('\tTab') # \t addas one tab space before string
# print(r'\tTab') # r - raw

# pattern =re.compile(r'abc')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
#     print(match.start(), match.end(), match.group())
#     print(type(match))
#
# print(text_to_search[1:4]) # returns text from that index
# print(text_to_search[264:267]) # use with for match in matches: print(match) and take indexes from there

#___________________________________
# pattern =re.compile(r'.')   # to search for "." we need to user (r'\.') with ('.') it will search for each character
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match.group())

#_______
# pattern =re.compile(r'example.com')   # will find example.com or example-com , because . means what ever object except next_line .to search with '.' use  example\.com
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match.group())

#__________________
# pattern =re.compile(r'\s')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

#___________
# pattern =re.compile(r'\BHa') # searches for Ha but not in the beginning of word, word search in the beginning of word use \bHa
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
# print(text_to_search[71:80])
# print(text_to_search[76:86])
# print(text_to_search[78:88])

#__________________________
# pattern =re.compile(r'^Start') #
# matches = pattern.finditer(sentence)
# for match in matches:
#     print(match)

#_________________________
# pattern =re.compile(r'\d') # (r'\d\d') will return each two numbers in a row to search for all tel numbers (r'\d\d\d.\d\d\d.\d\d\d\d')
# # using '.' between \d will find all numbers , if we want to find specific we use '-' or something else instead of '.'
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

#________________________
# pattern =re.compile(r'\d\d\d[-*]\d\d\d[-*]\d\d\d\d') # using [-*] it means find with '-' or '*'
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

#_____________
# pattern =re.compile(r'[13]\d\d[-*\.]\d\d\d[-*\.]\d\d\d\d') # using [13] returns numbers which start with 1 or 3 and between numbers are '-' or '8' or '.' . .
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

#________________
# pattern =re.compile(r'[1-5][1-9]') # using [1-5] searches numbers which start with 1 between 5  and second digit is between 1-9 .
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

#____________
# pattern =re.compile(r'[a-zA-Z]') # using that will return all which start between small a-z and capital A-Z .
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

#______________________
# pattern =re.compile(r'[^w]all') # returns all except wall, because ignores w
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

#______________________
# pattern =re.compile(r'\d{3}.\d{3}.\d{4}') # \d{3} means that first three symbols must be three numbers in row, \d{5,8} will search for number in a row between 5 - 8 .
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

#________________________Group - ()
# pattern =re.compile(r'M(rs|s|r)\.?\s[A-Z]\w*') # to search for Mr, Mrs, Ms then . and might be space and name starts from A-Z and then nothing, you may user space like that - [ ] .
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)






#__________________NEXT
# import re
#
# emails = '''
# SampleMaiL@example.com
# john.sample@my-work.net
# jack-125-production@colledge.edu
# bob.Samples@example.co.uk
# example@example.org
# '''
#
# urls = '''
# https://www.google.com
# http://www.wordpress.org
# https://www.nasa.gov
# https://example.net
# www.example.net
# example.net
# '''

#______email search
# pattern = re.compile(r'[a-zA-Z0-9][a-zA-Z0-9_\-\.]+@[a-zA-Z0-9][a-zA-Z0-9\-]+\.\w{2,3}(\.\w{2,3})?') # + means that after that there might be symbols
# matches = pattern.finditer(emails)
# for match in matches:
#     print(match)

#____site search
# pattern = re.compile(r'(http://|https://)?(www\.)?(\w|-)+\.\w+') # | - means or , ? means might be or not, or (r'(http://|https://)?(www\.)?(\w|-)+\.\w{2,3}')
# # OR (r'(http://|https://)?(www\.)?(\w|-)+(\.\w+)')
# matches = pattern.finditer(urls)
# for match in matches:
#     print(match)

#______ SUB groups
# pattern = re.compile(r'(http://|https://)?(www\.)?((\w|-)+)(\.\w+)')
# subbed_urls = pattern.sub(r'\1\2\3\4', urls) # - \1\2 - are groups and returns them
# print(subbed_urls)
# matches = pattern.finditer(urls)
# for match in matches:
#     print(match.group(3))   # if we use (1), (2), (3), (4) it will print a group, because in compile we have 4 groups, each  separated by ()


#________ NEXT
import re


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Mr. JONES
abc
hall mall wall ball
'''

sentence = 'Start a sentence and then bring it to an end'


# pattern = re.compile(r'')
# pattern =re.compile(r'M(rs|s|r)\.?\s[A-Z]\w*')
# pattern =re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern =re.compile(r'(\d{3}).(\d{3}).(\d{4})') # items are grouped
# matches = pattern.findall(text_to_search) # returns only values we searched for

# print(matches)

#____________________________
# pattern = re.compile(r'bring')
#
# matches = pattern.search(sentence) # returns if matched or not
# print(matches)


#__________________
# pattern = re.compile(r'start', re.IGNORECASE) # ignores if start is written with s or S !
# matches = pattern.findall(sentence)
#
# print(matches)

#_________________
pattern = re.compile(r'^M', re.MULTILINE) # will use ^ not for whole text, but for each line!
matches = pattern.findall(sentence)

print(matches)
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)