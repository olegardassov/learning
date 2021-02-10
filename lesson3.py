# some_string = ''
# some_string2 = ""
# some_string3 = ''''''
# some_string4 = """"""
#
# wrong_string = 'that's'
# some_string5 = 'that\'s'
# # must be "that's"
# # or 'that\'s' \ знак исключения
# # if you copy some text it is better to use """""" because it probably won,t be used in copied text
#
#
empty_string = ' '
string_sample = "Hello world world"
string_sample2 = "first letteR is lowErcase"
string_sample3 = "extra whitespace string"
german_sample = "der Flub"
#
# #print(string_sample[0:5]) # to write whole word we write [0:5] 0 is first letter and 5 is last but it won,t write last letter,  it will write until 4 letter
# # you can also use -1, -2 and etc
# print(string_sample[-1])
# print(string_sample[-5:-1]) # we still have to write from left to right
# print(string_sample[-5:]) # it will write from letters from the end of the line , you can use 5 or -5
# print(string_sample[:5]) # it will take from the beginning of the sentence 5 letters
# print(string_sample[:]) # the same as print(string_sample)
#
# print(string_sample[0:10:2]) # he will take from the beginning 9 letters and write each second letter print(string_sample[0::2] 2 is number of symbol he will write
# print(string_sample[::-1]) # the text will be written backwards  -1 is each letter, -2 will be each second letter
# test_string2 = "hello"
# test_string = 'Hello world. It is beauftiful day.'
# print(test_string[0:11])       # it will print Hello world
# print(test_string[-4:-1])    # it will print day
#
# print(test_string[0:5], test_string[19:29])  # to print only first and third word , you can also use + but then you have to make a space
# print(test_string[0:5] + ' ' + test_string[19:29])
#
# print(len(test_string))  # to count number of symbols in text
# to count number you have to write
# print(len("24564"))
#
# print(test_string.find("world")) # using this command we know from what symbols the word starts
# print(len("world"))  # from that command we know that word is 5 symbols long
# print(test_string[6:11]) # we print only word world

# search command only finds first word in text, if there is two words, he will give tyou only first one

# print(test_string.upper()) # all symbols will be upper
# print(test_string.lower()) # all symbols will be lower
# print(german_sample.lower())
# print(german_sample.casefold())  # writes all in lower cases,  there might be difference if there are some special symbol used in text
# print(test_string2.capitalize())   # first letter will be upper case

# print(test_string[0:5].upper(), test_string[5:]) # he writes first word in upper cases and second test_string prints all other words of the sentence
#
#
# print(test_string.split()) # it splits all sentence into words

# user_name = 'olEg'
# print(user_name.lower().capitalize()) # instead of olEg he write first letter big and E lower case = Oleg . in that case of command he changes name only once
# #alternative for previous command
# user_name = user_name.lower().capitalize()   # if we want to change forever, we have to use command like that.
# print(user_name)
#
# print(user_name.capitalize().lower()) # if you use capitalize first the lower command  will make all letters  lower because it is last command

# print(string_sample.count('world')) # will find word and let you know from which symbol this word starts
# print(string_sample.find('world')) # it will count how many those words or symbols are there in whole text, but it is case sensitive
# print(string_sample.find('o'))
# print(string_sample[0:7].find("world")) #it will search only between first 6 letters
#
# # or
# search_string = "world"
# print(string_sample.count(search_string))

# print('world' in string_sample) # to check if there is such word in our text
#
# print(string_sample + string_sample2)
# print(string_sample + " " + string_sample2) # you cannot add numbers
# print(string_sample, string_sample2) # in that case you can use numbers also

# worker = 'John'
# worker2 = 'Mary'
# salary = 1000
# salary2 = 2000
# worker_string = "'s salary is"
# print(worker + worker_string, salary)
# print(worker2 + worker_string, salary2)
#
# print("{}'s salary is {}".format(worker, salary)) # {} {} those are words from format(worker, salary)
#
# worker_string2 = "{}'s salary is {}"
# print(worker_string2.format(worker, salary)) # we can solve thise like those two lines
# # or like that
# print(worker_string2.format("Oleg", 2000))
# worker_string3 = "{1}'s salary is {0}" # text order is changed here
# print(worker_string3.format(worker, salary)) # in that case he changes the order of the text
#
# apples = 3
# bananas = 5
# pears = 2
# fruit_string = "John has {} bananas, {} apples and {} pears"
# fruit_string2 = "John has {1} bananas, {0} apples and {2} pears" # changes the order of the fruits
# print(fruit_string.format(bananas, apples , pears))
# print(fruit_string2.format(bananas, apples , pears)) #in this case order is changed

# price_string = "This {product:} costs {price:.2f} euros"   # .2f is two numbers after dot like 1500.00
# print(price_string.format(price=350, product='computer'))
#
# temperature = 35
# if temperature < 30:
#     print("it is cold today")
# elif temperature > 30:
#     print("it is hot today")

# id_code = input('Please eneter your national id: ')
#
# if len(id_code) == 11:
#     print('Your ID code is', id_code)
# elif len(id_code) > 11:
#     print('code you entered is longer than 11 digits')  # elif and else are not needed, we can do without them
# else:
#     print('Code you entered is shorter than 11 digits')  # else might be used without elif
#
# some_string = "Hello world. It is a beautiful day"
# # some_string = 1500
# print("Please input word beautiful: ")
# beautiful = input()
# if "beautiful" in beautiful:
#     print('true')
# else:
#     print('false')
#
# #if len(some_string[0:5] > 10):   # we can use
# if len(some_string) > 10 or len(some_string) < 5: # that way we can use and, or , not commands. we can use if 100 > 10 or 100 < 10
#     print("some string is greater than 10 characters")
# elif len(some_string) > 20:
#     print("some string is also greater than 20 characters")
#
# if some_string == "Hello world. It is a beautiful day":
#     print(True)

# some_string = "Hello world. It is a beautiful day"
some_string = 1500.0               # to check if it is text or numbers

if type(some_string) == str: # to check if it is text or numbers also can be used int for number, float for number with .0 and str for text
    print("yes")
else:
    print("no")
