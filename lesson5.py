# #for loop
# people = [["John", 'New York', "35", 'male'], ['Alex', 'Moscow', '21', 'male'],
#           ['Annika', 'Tallinn', '30', 'female'], ['Piere', 'Paris', '42', 'male']]
#
# for person in people:
#     if person[3] == 'male': # person[3] is index of the forth word in each list (gender)
#         print('This is' + person[0] + '. He lives in ' + person[1] + '. He is ' + person[2] + ' years old')
#     elif person[3] == 'female':
#         print('This is' + person[0] + '. She lives in ' + person[1] + '. She is ' + person[2] + ' years old')
# else:
#     print('Reached end of list')



# while True:
#     print("I can,t stop!!!")


#_______________________           by that I separate programs
# counter = 0
#
# while counter < 100:    # counts until 99 , if I want to count until 100 I need while counter <= 100:
#     print('I can,t stop!!!', counter, 'times')
#     counter = counter + 1  # or counter += 1

#_______________________

# counter = 0
#
# while counter <= 10000: # counts until 99 , if I want to count until 100 I need while counter <= 100:
#     counter += 1
#     if counter % 100 == 0: # in that case he write each 100 step : 100, 200, 300 and so on
#         print(counter)
#
#
# #_______________________
#
# if you enter code under or over 11 symbols it loops with please try again. if you input 11 symbols it prints your inputed text
# condition = True
# while condition:
#     user_input = input('Please enter id: ')
#     if len(user_input) != 11:
#         print('Please try again')
#     else:
#         print(user_input)
#         condition = False

# #_______________________

#
# while True:
#     user_input = input('Please enter id: ')
#     if len(user_input) != 11:
#         print('Please try again')
#         continue  # continues until condition met
#     else:
#         print(user_input)
#         break  # break comes out of the loop

# #_______________________
#TRY      try must be always used with except       to understand the error we get, in new file try code you are trying to get error from and check in output
# user_input = input('Please eneter your ID:' )
# try:
#     user_input = str(int(user_input))  # if I write str(int(user_input) it will make it to int and then back to str and in future use it as string
#     if len(user_input) != 11:
#         raise UserWarning
#     else:
#         print(user_input)# using raise we can call different Errors
# except ValueError:  # if try could not do that, we will go to except       except: might be used like this, it will work for all errors
#     print('Raised error')
#
# except UserWarning:
#     print('Value you entered is too long or too short! ')
#
# finally:  # it is text which comes always in the end of the program
#     print('Program finished working! ')


#NEXT SAMPLE

# user_input = input('Please eneter your ID:')
# try:
#     user_input = str(int(user_input))  # if I write str(int(user_input) it will make it to int and then back to str and in future use it as string
#     if len(user_input) != 11:
#         raise UserWarning
#     else:
#         print(user_input)  # using raise we can call different Errors
#
# except:  # if try could not do that, we will go to except       except: might be used like this, it will work for all errors
#     print('ID code is too short or too long')
#
# else:  # else will work only if try is successful
#     print('Some other error happened')
#
# finally:  # it is text which comes always in the end of the program
#     print('Program finished working! ')

#NEXT SAMPLE
condition = True
while condition:
    user_input = input('Please eneter your ID:')
    try:
        user_input = str(int(user_input))  # if I write str(int(user_input) it will make it to int and then back to str and in future use it as string
        if len(user_input) != 11:
            raise UserWarning
        else:
            condition = False

    except:  # if try could not do that, we will go to except       except: might be used like this, it will work for all errors
        print('ID code is too short or too long')

    else:  # else will work only if try is successful
        print('Your national id is ', user_input)

    finally:  # it is text which comes always in the end of the program
        print('Program finished working! ')


