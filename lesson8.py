#_________Dictionary
# dictionary cannot be indexed.

# dictionary_var = {"Name" : "Oleg", "Age" : 30, 5 : "Hello"}
# print(dictionary_var["Name"])
# print(dictionary_var[5])
#
# x = 5
# student = {"name" : "John", 'age' : 32, "courses" : ["Math", "Art", 'Programming'], 1 : "int key", 0.2 : "float key", x : "variable", "var_key" : x}
# print(student["courses"][1])   # you can use like this
# print(student[x])
# print(student[5])   # in that case because x = 5 and in students x : "variable we can print like that
# print(student['var_key'])   # var_key = x and x = 5 so we get 5 when we print var_key
#
# print(student.get('job'))   # if we do not have job in our dictionary , we get NONE. if we print without .get we will get an ERROR
# print(student.get('job', "ERROR"))  # it will print ERROR.

#_____________________________ adding one elelment to dictionary
# x = 5
# student = {"name" : "John", 'age' : 32, "courses" : ["Math", "Art", 'Programming'], 1 : "int key", 0.2 : "float key", x : "variable", "var_key" : x}
# student["name"] = "Jack" # in that case name from John will be replaced by Jack
# student["job"] = "Programmer"  # using that we can add new dictionary element to our student dictionary!
# print(student['job'])  # now it will return that job is programmer

#_________________________________________________________ adding to and updating existing dictionary
# x = 5
# student = {"name" : "John", 'age' : 32, "courses" : ["Math", "Art", 'Programming'], 1 : "int key", 0.2 : "float key", x : "variable", "var_key" : x}
#
# print(student)
# student.update({'name' : "Michael", "age" : 27, "phone" : "555-5555"})  # it replaces existing dictionary by new and adds new ones also.
# print(student)
#
# del student['name']   # deletes name from student dictionary forever!
# print(student)
#
# popped_item = student.pop("age")  # we delete age but we save it to variable and can use it in future
# print(student)
# print(popped_item)
# print(len(student))  # returns number of elements in dictionary

#_____________________ getting information from dictionaries
# x = 5
# student = {"name" : "John", 'age' : 32, "courses" : ["Math", "Art", 'Programming'], 1 : "int key", 0.2 : "float key", x : "variable", "var_key" : x}
#
# print(student.keys())   # will return all keys in dictionary
# print(student.values()) # Will return all values
# print(student.items())
#
# for x in student.items():    # can be used all keys,values, items. prints each value in a row
#     print(x)
#
#
# for key, value in student.items():
#     print(key, value)

#____________________________________
# x = 5
# student = {"name" : "John", 'age' : 32, "courses" : ["Math", "Art", 'Programming'], 1 : "int key", 0.2 : "float key", x : "variable", "var_key" : x}
#
# print(student.keys())   # will return all keys in dictionary
# print(student.values()) # Will return all values
# print(student.items())
#
# some_list = [[1, 2 ,3], [3, 4, 6], [5, 6, 7]]
# for key, value, something in some_list:    # key is for 1, value is for number 2 and something is for number 3
#     print(key, value, something)
#
# for x in some_list:
#     print(x)


#___________________________________ Working with files



