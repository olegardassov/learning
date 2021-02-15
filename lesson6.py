
x = int(5)
print(x)
pr
# def id_check(id_code, chk_list):
#     counter = 0
#     result = 0
#     for num in chk_list:
#         result += int(id_cide[counter] * num)
#         counter += 1
#     return result % 11
#
# id_code = list(input('Please enter your id: '))
#
# chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
#
#
# if id_check(id_code, chk1) == 10:
#     result = id_check(id_code, chk2)
#     if result == int(id_code[10])
#         print('ID code is valid')
#     else:
#         print("ID code is invalid")
# elif id_check(id_code, chk1) == int(id_code[10]):
#     print('ID code is valid')
#
#
#
# #______________________________________________________________________________
#
# print(id_check(id_code, chk1))


# id_code = input('Please enter your ID code: ')
# chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# chk2 = [3, 4, 5, 6, 7, 8, 9 ,1, 2, 3]
# id_code_list = list(id_code)    # to convert string on int,float to list
# # print(id_code_list)
#
# counter = 0
# result = 0
# for num in chk1:
#     result = result + chk1[counter] * int(id_code_list[counter])   #   0 + 1 * 3 = 3 + 2 * 9 = 21 + 3 * 0 = 21 + 4 * 0 = 21 + 5 * 5 = 46 and so on
#     counter += 1
# # print(result)
# check_num = result % 11
#
# if check_num == int(id_code[-1]):
#     print('ID code is valid')
# elif check_num == 10:
#     counter = 0  # because counter is 10 from the last for cycle
#     result = 0  # because result is sum (86) from the last for cycle
#     for num in chk2:
#         result = result + chk2[counter] * int(id_code_list[counter])  # 0 + 1 * 3 = 3 + 2 * 9 = 21 + 3 * 0 = 21 + 4 * 0 = 21 + 5 * 5 = 46 and so on
#         counter += 1
#     check_num = result % 11
#     if check_num == int(id_code[-1]):
#         print("ID code is valid")
#     elif check_num >= 10:
#         check_num = 0
#     else:
#         print('ID code is invalid')
# else:
#     print('ID code is invalid')


#____________ FUNCTIONS  # functions are always written in the beginning of the program

# for letter in "Python" :
#     if letter == "h" :  # it writes all letters from Python, skips 'h' and then contiunes to print other letters
#         continue
#     print('Current letter :', letter)
#
# var = 10
# while var > 0:
#     var = var -1
#     if var == 5:
#         continue   # it works like skip, when it get to number 5 it skips it and count next numbers
#     print('Current variable value: ', var)
# print('Good bye!')


# def squares(x):  # in that case if we write like squares(5) it will put that number to squear
#     x = x ** 2
#     print(x)
# squares(5)


# def squares(number):  # in that case squares becomes number we will choose
#     number = number ** 2
#     return number
#
# def double(number, multiplier):
#     result = number * multiplier
#     return result
#
# for number in range(1, 101):
#     print(squares(number))      # it print square from each number from range of 1 to 100
#
# print(squares(5))  # it will print 25 , because 5 ** 2 = 25
# print(squares(10))
# print(type(squares(2)))
# print(double(2, 4))

#________________________________

# def area(a, b):
#     area = a * b
#     return area
#
# def perimeter(a, b):
#     perimeter = 2 * (a + b)
#     return perimeter
#
# def print_message(name, age, profession):
#     return print("Hi, my name is", name, ". I am", age, 'years old. I work as a', profession, '.')
#
# def no_parameters():
#     x = 25 ** 0.5
#     return x
#
# side_a = 5
# side_b = 10
#
# print(area(side_a, side_b))     # we use our variables from list
#
# user_name, user_age, user_profession = input("Enter name, age and profession divided by space: ").split(' ')    # split makes list of inputed items and prints them
# print_message(user_name, user_age, user_profession)

#______________________


employee = ['John', 'Smith', '32', '5000', 'Tallinn']

def print_employee_message(employee_data):
    name = employee_data[0]
    last = employee_data[1]
    age =  employee_data[2]
    salary = employee_data[3]
    town = employee_data[4]
    print('Hello ' + name + ' ' + last + '. Your are ' + age + ' years old. Your salary is ' + salary + 'EUR. You are from ' + town + '.')
    #or
    return 'Hello ' + name + ' ' + last + '. Your are ' + age + ' years old. Your salary is ' + salary + 'EUR. You are from ' + town + '.'

print_employee_message(employee)
print(print_employee_message(employee))