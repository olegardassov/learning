# #map() method
#
# def square(x):
#     return x ** 2
#
# # long solution
# int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = []
# for x in int_list:
#     new_list.append(square(x))
#
# print(new_list)
#
# # another solution, easier one
# print(list(map(square, int_list)))
# print([square(x) for x in int_list])
# print([square(x) for x in int_list if x % 2 == 0])

#_______________________________________________________

#zip() method
# data1 = [100, 200, 300, 400, 500, 600, 700]
# data2= ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#
# new_list = []
# cnt = 0
# for x in data1:
#     new_list.append([x, data2[cnt]])
#     cnt += 1
#
# print(new_list)
#
# #easier version
#
# # combination = list(zip(data1, data2))
# # print(combination)
#
# #_____________
# combination = list(zip(data1, data2))
# for x, y in combination:
#     print(x, y)
#
# #______________
# combination = list(zip(data2, range(10)))
# print(combination) #returns index of elements
# print(combination[0])
# print(combination[1][0])

# #_____________Collections
# from collections import Counter
#
# sample_string = "aaaabbbbbccccdddddeeeeffff"
# my_counter = Counter(sample_string)
# print(my_counter)   #returns elements from string and counts them in decreasing order
# print(my_counter['a']) #returns how many times is 'a' in our string
# print(my_counter.values()) # returns keys
# print(my_counter.keys()) # returns values (how many times) we meet same symbol
#
# print(my_counter.most_common()) # you can use number in (3) to get top3
# print(my_counter.most_common(3)[1]) # we can index it
#
# print(my_counter.elements())
# for x in my_counter.elements():
#     print(x)
#
# print(list(my_counter.elements()))  # returns list of sample_string symbols


#____________________________________namedtuple
# from collections import namedtuple
# Point = namedtuple('Point', 'x,y')
# pt = Point(5, -2)
# print(pt)



# #___________________________________OrderedDict
# from collections import OrderedDict
#
# some_dict = {'Name': 'Jack', 'Surname': 'Smith', 'Age': 30}
# print(some_dict)
#
# #______________
# ordered_dict = OrderedDict()
# ordered_dict['Name'] = 'Jack'
# ordered_dict['Surname'] = 'Smith'
# ordered_dict['Age'] = 30
# print(ordered_dict) # cannot be returned with index


# #______________________defaultdict
# from collections import defaultdict
#
# defaultdict = defaultdict(int)
# defaultdict['a'] = 100
# defaultdict['b'] = 200
# print(defaultdict)
# print(defaultdict['c']) # we do not have key ['c'], it returns 0 .

# #____________________deque
# from collections import deque
#
# d = deque()
# d.append(1)
# d.append(2)
# print(d)
#
# d.appendleft(3) # add to beginning
# print(d)
# d.append(4) # adds to end
# print(d)
# d.popleft() # deletes first value from list
# print(d)
#
# d.extendleft([7, 8, 9])
# print(d)
#
# d.rotate(1) # all numbers move to 1 position to the right. last number becomes first. using (x) can be 1 or -1 etc . with -1 moves to left.
# print(d)
# d.rotate(-1) # in case of d.rotate() default is 1
# print(d)
#
# d.insert(0, 5)  # adds number 5 as first number
# print(d)



#__________________itertools
import itertools

counter = itertools.count()

data = [100, 200, 300, 400]

# print(next(counter))    # adds + 1 each time you call that command
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# #___________________
#
# data_sample = zip(itertools.count(), data)
# for x in data_sample:
#     print(x)
#
# #____________________
#
# data_sample2 = zip(data, range(10))
# for x in data_sample2:
#     print(x)
#
# #______________________
#
# data_sample3 = itertools.zip_longest(data, range(10))
# for x in data_sample3:
#     print(x)

#____________________

# counter = itertools.count(start=1, step=5)  # start , number from what to start, step is + how many if start 1 and step 5 =1, 6, 11, 16, 21 etc
# print(next(counter))    # adds + 1 each time you call that command
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#
# counter = itertools.count(start=1, step=5) # start , number from what to start, step is + how many if start 1 and step 5 =1, 6, 11, 16, 21 etc
#
# for x in counter:
#     if x < 10:
#         print(x)
#     else:
#         pass

#_____________________

# counter = itertools.cycle([1, 2, 3])    # counts 1,2,3,1,2,3,1,2,3
# print(next(counter))    # adds + 1 each time you call that command
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#
# #________________
# counter = itertools.cycle(('On', 'Off'))    # counts On,Off,On,Off,On,Off
# print(next(counter))    # adds + 1 each time you call that command
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# #_______________________
# counter = itertools.repeat(4, times=3)  # counts number 4 three times. print must be == to times
# print(next(counter))
# print(next(counter))
# print(next(counter))


# #____________
# def squared(x):
#     return x ** 2
# result = map(squared, range(10))
# # print(result)   #returns type of result
# # print(list(result)) # returns list of numbers
#
#
# result2 = itertools.starmap(pow, [(2, 2), (5, 2), (10, 2)]) # returns (x, y) = x ** y
# print(list(result2))
#
#
# print(pow(2, 2)) # returns 2 ** 2. 2 in step 2 = 4
#
#
# result3 = map(pow, range(10), itertools.repeat(2)) # returns (x, y) = x ** y
# print(list(result3))

#_________________

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
numbers2 = [1, 4, 5, 4, 3, 2, 1 ,0, 4]
selectors = [True, True, False, True]
names = ['Jack', 'John']

def more_than_two(x):
    if x > 2:
        return True
    return False



#___________________________

# for num1 in numbers:  # all available  combination method
#     for num2 in numbers:
#         for num3 in numbers:
#             for num4 in numbers:
#                 print(num1,num2,num3,num4)

#__________________________

# result = itertools.combinations(letters, 2) # order is not critical , not sure, must check
# for x in result:
#     print(x)


#__________________________not sure, must check

# result = itertools.permutations(letters, 3) # order is critical (letters, 3 - is number of combinations) 3 - is combination of 3 symbols
# for x in result:
#     print(x)

# #___________________
# result = itertools.product(letters, repeat=2) # all available combinations
# for x in result:
#     print(x)

#___________________
# result = itertools.combinations_with_replacement(numbers, 4) # order is not critical
# for x in result:
#     print(x)

# #__________________
# new_list = []
# new_list.extend(letters)
# new_list.extend(numbers)
# new_list.extend(names)
# print(new_list)
# for x in new_list:
#     print(x)
#
# ##OR
#
# combined = itertools.chain(letters, numbers, names)
#
# for x in combined:
#     print(x)


#_______________
# combined = itertools.islice(range(10), 5) # returns slice from 0 to 5
# print(list(combined))
#
# combined = itertools.islice(range(10),3, 5) #returns slice from 3 to 5
# print(list(combined))


#______________



# result = itertools.compress(letters, selectors) # checks letters to selectors(boolean) and returns those which are True in selectors
# for item in result:
#     print(item)


# result2 = filter(more_than_two, numbers)
# for x in result2:
#     print(x)

# #____________
# result3 = itertools.filterfalse(more_than_two, numbers)
# for x in result3:
#     print(x)



#_________________________

# result = itertools.dropwhile(more_than_two, numbers2)   # more_than_two is defined upwards with variables , returns all numbers which are after False
# for item in result:
#     print(item)
#
#
# result = itertools.takewhile(more_than_two, numbers2)   # returns numbers which are before False
# for item in result:
#     print(item)


#_________________________

# result = itertools.accumulate(numbers2) # = 1 + 4 = 5 , 5+5 = 10, 10+4 = 14 etc
# for x in result:
#     print(x)




#_______________________________________NEW
import itertools

def get_city(person):
    return person['city']

people = [
    {
        'name': 'John Smith',
        'city': 'Berlin'
    },
    {
        'name': 'Mary Gold',
        'city': 'Berlin'
    },
    {
        'name': 'Taavi Tamm',
        'city': 'Berlin'
    },
    {
        'name': 'Piere Cardin',
        'city': 'Tallinn'
    },
    {
        'name': 'Jack Rock',
        'city': 'Tallinn'
    },
    {
        'name': 'Lee Hong',
        'city': 'Tallinn'
    },
    {
        'name': 'Abdul Faruh',
        'city': 'Dubai'
    },
    {
        'name': 'Mary Pierce',
        'city': 'Dubai'
    },
    {
        'name': 'John Sumers',
        'city': 'Tallinn'
    }
]

result = itertools.groupby(people, get_city)
#
# for key, group in result:
#     # print(key, group)
#     # for person in group:
#     #     print(person)
#     # print()
#
#     print(key, len(list(group)))    # returns how many people from what cities, for command above must be commented
#
#__________________________

