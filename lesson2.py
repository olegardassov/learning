# name = "oleg"
# print(type(name))
# integer2 = 216
# integer = 234
# print(type(integer))
#
# float2 = 10.1
# print(type(float))
# sum = int(integer) + int(integer2) + float(float2)
# print(sum)
#
# boolean = True
# print(type(boolean))
#
# none_value = None
# print(type(none_value))
# none_value = None
# print(help(none_value))
#
# a = 500
# b = 250
# print(a + b)
# print(2 + 2)
# print(a + 100)
# print(a + 20.8)

# print(a - b)
# print(3 - 1)
# print(a - 100)
# print(a - 5.0)
#
# print(500, '600') #500 600
# print(500, '720', True) # = 500 720 True

# print(a * b)
# print(2 * 2)
# print(a * 2)
# print(a * 0.2)
# print(a + 5)

# print(a / b)
# print(type(a / b))
# print(8 / 2)
# print(a / 250)
#
# print(a // b)
# print(5 // 2)
# print(a // 150)
#
# print(a ** b)
# print(5 ** 2)
# print(a ** 2)
# print(25 ** 0.5) #tak mozno vqvesti koren iz ljubogo 4isla, berem 4islo i vozvodim v stepen 0.5
# a = 500
# b = 150
# print(a % b)
# print(5 % 2)
# print(a % 150)   # pri delenii 10 na 7 ostatok budet 3 , eto i est otvet.

# number = 123
# some_text = 'some string'
# print(number, some_text)
# number2 = str(number)
# print(type(str(number)))
# print(type(number))
# print(type(number2))
# print(some_text + number2)

# some_string = '555'   # you can convert from text only numbers to numbers True = 1 , False = 0
# print(int(some_string))
# print(float(some_string))  # we can use float

# some_string = "-500"   # to get False you can use "" , some_string = ''
# print(bool(some_string))
# converting boolean if it is 0 it is false, if it is some number except 0 it is true, it might be -500 etc

# print(100) # int
# print(0.2) # float
# print('Hello world') # str
# print(True) # bool
#
# a = 'String inside variable'
# print(a) # variable
# a = 'String inside variable'
# print(str(100) + ' ' + str(0.2) + ' ' + 'Hello world ' + str(True) + ' ' + a)

# print(type(input())) # all inputed text by user is accepted as string

# print(input('Please enter some text: '))
# print(user_input)

# print(len('Oleg')) # counts how many letters is there in the word
# print(len('123456')) # we cannot count numbers directly , but we can do it as a text(str)


# a = 5
# b = 4
# c = 3

# a = (float(input('a: ')))   # we need to conver inputed text from string to number(float)
# b = (float(input('b: ')))
# c = (float(input('c: ')))
#
#
# P = (a + b + c) / 2 # if I would have used // the answer would be 6 , not 6.0
# print(P)
#
# triangle_area = (P * (P -a) * (P - b) * (P - c)) ** 0.5
#
# print(triangle_area)

a, b, c = input(' input all three sides:').split(' ') #split can be used only with one input , you cannot use float additionally
print(a)
print(b)
print(c)

P = (float(a) + float(b) + float(c)) / 2 # if I would have used // the answer would be 6 , not 6.0
print(P)

triangle_area = (P * (P -float(a)) * (P - float(b)) * (P - float(c))) ** 0.5


