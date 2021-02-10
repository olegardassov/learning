#LIST

# empty_list = []
# empty_tuple = ()
# empty_dict = {}
# empty_set = set()
#
# print(type(empty_set))
# print(type(empty_set))
#
# empty_list = [1233, 12.313, 'Some string', True, None, ['One', 'Two', 3]]
# print(empty_list)  # to print only 'Some string' we can use print(empty_list[2])
# print(empty_list[5][1]) # we will get from ['One', 'Two', 3] only 'Two'
# print(empty_list[1:4])  # will print from second word to forth
#
# empty_list[2] = 'New string'
# print(empty_list)   # in that case 'Some string' gets new name = 'New string'
#
# list_element = [1233, True, 'another string'] # variable
# empty_list = [1233, 12.313, 'Some string', True, list_element, ['One', 'Two', 3]] # we use variables as well (list_element)
# print(empty_list)
#
# print(empty_list[::-1]) # it will print from back to front
#
# courses = ['History' , 'Math', 'Literature', 'Physics', 'Programming']
#
# print(len(courses)) # in case of list we will get number of lists, not symbols
# courses[0] = 'Art' # to replace one of the subjects
# print(courses)
#
# courses.append('Art') # to add new subject in list
# print(courses)
# # or
# new_course = 'Art'
# courses.append(new_course)
# print(courses)

# new_course = 'Art'
# courses.insert(0, new_course) # to add as first or inbetween 0 - first, 1 - second and so on also can be used (0, 'Art')
# print(courses)
#
#
# courses2 =  ['Econimics', 'Marketing'] # to add into end of the list
# courses.extend(courses2)
# print(courses)
# # or
# print(courses + courses2)
# print(len(courses)  # in that case course is changed only once
#
# # in that case we change it forever, because we save it as new variable
# courses = courses + courses2
# print(courses)
# print(len(courses))

# courses.remove('Math') # removes subject from list, removes forever. you need to tell him, what exactly you want to remove
# print(courses)

# courses1 = ['History' , 'Math', 'Literature', 'Physics', 'Programming', ['Economics', 'Marketing', 'Math']] #  ['Economics', 'Marketing', 'Math'] is list in a list
# courses2 =  ['Economics', 'Marketing', 'Math']
# courses1[5].remove('Economics') # in that case we can remove Economics from list in our list
# print(courses1)
# #courses1[5].append('Economics') # to add 'Economics' into list in our list
#
#
# courses1.pop()   # always removes last element from the list
# print(courses1)
#
# popped_item = courses1.pop() # we make it variable, if we will have to use it somewhere in a future
# print(courses1)
# print(popped_item)
#
# courses3 = ['History' , 'Math', 'Literature', 'Physics', 'Programming', ['Economics', 'Marketing', 'Math']]
# courses3.reverse() # writes the line backward
# print(courses3)



# courses4 = ['Econimucs', 'Marketing', 'Math', "Art", 12, 54, 32, 'art'] # we cannot sort list like this
# numbers = [1, 5, 6, 7, 3 ,76, 23, 34]
# numbers.sort() # in that case he saves the new lsit and uses it in future as well
# print(numbers)  # to sort numbers in increasing
#
# courses2 =  ['Economics', 'Marketing', 'Math']
# courses2.sort()
# print(courses2) # sorts iz A-Z and then a-z
#
# setting = True
# courses2.sort(reverse=setting) # or courses2.sort(reverse=True)
# print(courses2)


#
# courses5 =  ['Economics', 'Art',  'Marketing', 'Math']
# print(sorted(courses5)) # sorts only once when prints. does not save anywhere
#
# courses6 =  ['Economics', 'Art',  'Marketing', 'Math', 'art']
# numbers2 = [1, 5, 6, 7, 3 ,76, 23, 34]
# print(min(numbers2)) # prints min number from list
# print(max(numbers2)) # prints max number from list
# max_number = max(numbers2)
# print(max_number)
# # can be also used for text
# print(min(courses6)) # sorts all list and then takes the first word from list, if you use max you will get last word
#
# print(courses6.index('Art')) # it is number 2 two word in list, but because it counts from 0 it is 1.
# #or like this
# art_index = courses6.index('Art')
# print(courses6[art_index])
#
#
# print('art' in courses6)

# numbers3 = [1, 5, 6, 7, 3 ,76, 23, 34]
# courses7 =  ['Economics', 'Art',  'Marketing', 'Math', 'art']
# print(courses7)
# print(type(courses7))
# #converting list into string>>
# courses_str = ', '.join(courses7) # to convert list into string, '' between you write, how list will be separated
# print(courses_str)
# print(type(courses_str))
# #backward converting
# new_list = courses_str.split(',')  # write, how you want the list to be separated
# print(new_list)
# print(type(new_list))
#
# some_string = 'hello, my name is oleg. I am 30 yaers old. I learn python. '
# new_list = some_string.split('. ') # it will  be speratated into list between each sentence
# print(new_list)

# list_1 = ['Math', 'History', 'Programming', 'Physics']
# list_2 = list_1.copy() # makes copy of list and doesn,t affect both lists
# print(list_1)
# print(list_2)
#
# list_1[2] = 'Sports'
# list_2[0] = ' Art'
#
# print(list_1)
# print(list_2)


#TUPLE -  cannot me modified. Like user name or something.

# courses9 = ('Economics', 'Marketing', 'Math', 'Art', 'art', 'Math')
# print(courses9)
# print(courses9[4])
# #courses[4] = 'Biology' # such command cannot be used
#
# courses10 = ('Biology', 'Programming')
# print(courses9 + courses10)
# new_courses = courses9 = courses10
# print(new_courses)
#
# new_list = list(courses9) # to modify TUPLE, we can convert it to list
# print(type(new_list))
# new_list[0] = 'Biology'
# new_tuple = tuple(new_list)
# print(new_tuple)
# print(type(new_tuple))  # in that case we can change tuple by converting it to list, modifieing and then changing it back to tuple.
# #Tuple can be used only with count and index command!




#SET if word is written 2 time, 'Set' always give you that word only single printed
# courses11 = {'Economics', 'Marketing', 'Math', 'Art', 'art', 'Math'} # each time you print it print in different order and if same word is used twice it prints it only once
# courses12 = ['Economics', 'Marketing', 'Math', 'Art', 'art', 'Math'] # list, it always print in same order
# print(courses11)
# print(courses12)
#
# print(list(set(courses12))) # converting into set (it deletes all same words, then we make it into list.
#
# courses11.remove('Economics') # you can delete words from 'Set'
# print(courses11)
#
# set1 = {'Math', 'History', 'Programming', 'Physics'}
# set2 = {'Art', 'Physics', 'Design', 'History'}
#
# print(set1.intersection(set2)) # looks for similar words in both sets , does not matter if set1 or set2 is first
#
# print(set2.difference(set1)) # in those two, there is a difference between what sets are you using this function
# print(set1.difference(set2))
#
# print(set1.union(set2)) # makes new set using unique words from both sets



#ITERATION (ITER) for cycle

# courses13 = ['History', 'Programming', 'Math', 'Literature', 'Physics']
#
# for subject in courses13: # subject is a name you choose by yourself, it can be what ever you want item, subject and so on
#     print(subject)
#
# numbers4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for num in numbers4:
#     print(num)  # if you print(numbers4) it will print numbers4 9 times.

numbers5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for num in numbers5:
    print(num)
    counter += 1 # or counter = counter + 1

print(counter)

numbers6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers6: # to print each count you need to use command inside the program
    print(num)


print('This is last element', num) # he will do that only on last count

numbers7 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers7:
    if num % 2 == 0:
        print(num)


for num1 in numbers7:
    for num2 in numbers7:
        for num3 in numbers7:
            for num4 in numbers7:
                print(num1, num2, num3, num4) # in that case we get all possible 4 digit codes with those numbers

letters = ['a', 'b', 'c','d']

if len(numbers7) > 5:       # in that case if number is divided 2 without ostatka, it write even, if not the odd
    for num in numbers7:
        if num % 2 == 0:
            print(num, 'Even')
        else:
            print(num, 'Odd')


if len(numbers7) > 5:       # in that case if number is divided 2 without ostatka, it write even, if not the odd
    for num in numbers7:
        if num % 2 == 0:
            if num > 5 and num < 12: # can be used 'and' 'or'
                print(num, 'Even and bigger than 5')
            else:
                print(num, 'Even')
        else:
            if num > 5:
                    print(num, "Odd and bigger than 5")
            else:
                    print(num, 'Odd')

                    






