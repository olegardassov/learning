# Домашнее задание:
#
# Написать программу с графическим интерфейсом.
# 1. В окно программы поместить произвольную картинку.
# 2. Поле для ввода и кнопку.
# 3. Пользователь вводит эстонский личный код.
# 4. Внизу программа выводит информацию о введёном коде. (пол, дата рождения, регион)
# 5. *добавить проверку валидности с помощью чекбокса (если галочка стоит, то проверяется валидность, если нету то не проверяется)
#
# P.S.
# Поле для ввода и чекбокс должны быть подписаны.
# Задание со звёздочкой не обязательно.

from tkinter import *   # imports all functions from tkinter


root = Tk() # creates program window
root.geometry('1150x820')

def Check():
    if var.get():
        id_code = user_entry.get()
        chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
        id_code_list = list(id_code)  # to convert string on int,float to list
        # print(id_code_list)

        counter = 0
        result = 0
        for num in chk1:
            result = result + chk1[counter] * int(
                id_code_list[counter])  # 0 + 1 * 3 = 3 + 2 * 9 = 21 + 3 * 0 = 21 + 4 * 0 = 21 + 5 * 5 = 46 and so on
            counter += 1
        # print(result)
        check_num = result % 11

        if check_num == int(id_code[-1]):
            valid = 'ID code is valid'
        elif check_num == 10:
            counter = 0  # because counter is 10 from the last for cycle
            result = 0  # because result is sum (86) from the last for cycle
            for num in chk2:
                result = result + chk2[counter] * int(id_code_list[
                                                          counter])  # 0 + 1 * 3 = 3 + 2 * 9 = 21 + 3 * 0 = 21 + 4 * 0 = 21 + 5 * 5 = 46 and so on
                counter += 1
            check_num = result % 11
            if check_num == int(id_code[-1]):
                valid = "ID code is valid"
                print(check_num)


            elif check_num >= 10:
                check_num = 0
            else:
                valid ='ID code is invalid'
        else:
            valid ="ID code is invalid"

        user_id = user_entry.get()
        print(user_id)
        try:
            user_id == str(int(user_id))
            # Check if ID code length is 11 symbols:
            if len(user_id) != 11:
                if len(user_id) > 11:
                    output = 'ID code is too long'
                elif len(user_id) < 11:
                    output = 'ID code is too short'
                    # pass     # , if I use pass, program will skip it and go on with program
                raise UserWarning
            else:
                condition2 = False
        except:
            print('ERROR')
            output_str = output + '\nERROR'
            print_output.set(output_str)

        else:

            # create variables for parts of ID code
            gender_id = user_id[0]
            birth_year = user_id[1:3]
            birth_month = user_id[3:5]
            birth_day = user_id[5:7]
            birth_region = user_id[
                           7:10]  # we can also make it birth_region = int(user_id[7:10]) , in that case we do not need to use if int(birth_range) in range(), we can use if birth_range in range()
            check_num = user_id[10]

            # IF statement to check gender and century of birth
            if gender_id == '1':
                gender = 'Male'
                birth_cent = '18'
            elif gender_id == '2':
                gender = 'Female'
                birth_cent = '18'
            elif gender_id == '3':
                gender = 'Male'
                birth_cent = '19'
            elif gender_id == '4':
                gender = 'Female'
                birth_cent = '19'
            elif gender_id == '5':
                gender = 'Male'
                birth_cent = '20'
            elif gender_id == '6':
                gender = 'Female'
                birth_cent = '20'
            else:
                gender = 'unknown'
                birth_cent = 'unknown'

            if int(birth_region) in range(1, 11):
                region = 'Kuressaare haigla'
            elif int(birth_region) in range(11, 20):
                region = 'Tartu Ülikooli Naistekliinik'
            elif int(birth_region) in range(21, 151):
                region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
            elif int(birth_region) in range(151, 161):
                region = 'Keila haigla'
            elif int(birth_region) in range(161, 221):
                region = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
            elif int(birth_region) in range(221, 271):
                region = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
            elif int(birth_region) in range(271, 371):
                region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
            elif int(birth_region) in range(371, 421):
                region = 'Narva haigla'
            elif int(birth_region) in range(421, 471):
                region = 'Pärnu haigla'
            elif int(birth_region) in range(471, 491):
                region = 'Haapsalu haigla'
            elif int(birth_region) in range(491, 521):
                region = 'Järvamaa haigla (Paide)'
            elif int(birth_region) in range(521, 571):
                region = 'Rakvere haigla, Tapa haigla'
            elif int(birth_region) in range(571, 601):
                region = 'Valga haigla'
            elif int(birth_region) in range(601, 651):
                region = 'Viljandi haigla'
            elif int(birth_region) in range(651, 701):
                region = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
            else:
                region = 'Unknown'

            print('Your national id is: ' + user_id)
            print('You are ' + gender)
            print('Your date of birth is ' + birth_day + '.' + birth_month + '.' + birth_cent + birth_year)
            print('You were born in ' + region)

            output_str = valid + '\nYou are ' + gender + '\nYour date of birth is ' + birth_day + '.' + birth_month + '.' + birth_cent + birth_year + '\nYou were born in ' + region + '\nYour check number is: ' + check_num + '\nValidation Successful'
            print_output.set(output_str)

    else:
        user_id = user_entry.get()
        print(user_id)
        try:
            user_id == str(int(user_id))
            # Check if ID code length is 11 symbols:
            if len(user_id) != 11:
                if len(user_id) > 11:
                    output = 'ID code is too long'
                elif len(user_id) < 11:
                    output = 'ID code is too short'
                    # pass     # , if I use pass, program will skip it and go on with program
                raise UserWarning
            else:
                condition2 = False
        except:
            print('ERROR')
            output_str = output + '\nERROR'
            print_output.set(output_str)

        else:

            # create variables for parts of ID code
            gender_id = user_id[0]
            birth_year = user_id[1:3]
            birth_month = user_id[3:5]
            birth_day = user_id[5:7]
            birth_region = user_id[
                           7:10]  # we can also make it birth_region = int(user_id[7:10]) , in that case we do not need to use if int(birth_range) in range(), we can use if birth_range in range()
            check_num = user_id[10]

            # IF statement to check gender and century of birth
            if gender_id == '1':
                gender = 'Male'
                birth_cent = '18'
            elif gender_id == '2':
                gender = 'Female'
                birth_cent = '18'
            elif gender_id == '3':
                gender = 'Male'
                birth_cent = '19'
            elif gender_id == '4':
                gender = 'Female'
                birth_cent = '19'
            elif gender_id == '5':
                gender = 'Male'
                birth_cent = '20'
            elif gender_id == '6':
                gender = 'Female'
                birth_cent = '20'
            else:
                gender = 'unknown'
                birth_cent = 'unknown'

            if int(birth_region) in range(1, 11):
                region = 'Kuressaare haigla'
            elif int(birth_region) in range(11, 20):
                region = 'Tartu Ülikooli Naistekliinik'
            elif int(birth_region) in range(21, 151):
                region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
            elif int(birth_region) in range(151, 161):
                region = 'Keila haigla'
            elif int(birth_region) in range(161, 221):
                region = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
            elif int(birth_region) in range(221, 271):
                region = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
            elif int(birth_region) in range(271, 371):
                region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
            elif int(birth_region) in range(371, 421):
                region = 'Narva haigla'
            elif int(birth_region) in range(421, 471):
                region = 'Pärnu haigla'
            elif int(birth_region) in range(471, 491):
                region = 'Haapsalu haigla'
            elif int(birth_region) in range(491, 521):
                region = 'Järvamaa haigla (Paide)'
            elif int(birth_region) in range(521, 571):
                region = 'Rakvere haigla, Tapa haigla'
            elif int(birth_region) in range(571, 601):
                region = 'Valga haigla'
            elif int(birth_region) in range(601, 651):
                region = 'Viljandi haigla'
            elif int(birth_region) in range(651, 701):
                region = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
            else:
                region = 'Unknown'

            print('Your national id is: ' + user_id)
            print('You are ' + gender)
            print('Your date of birth is ' + birth_day + '.' + birth_month + '.' + birth_cent + birth_year)
            print('You were born in ' + region)
            # output = StringVar()
            output_str = 'You are ' + gender + '\nYour date of birth is ' + birth_day + '.' + birth_month + '.' + birth_cent + birth_year + '\nYou were born in ' + region
            # mylabel = Label(root, textvariable=output)
            # mylabel.pack()
            print_output.set(output_str)







root.title('ID_CODE Checker!')  # name of program

root.iconbitmap('domo_icon.ico')    # changes icon of the program

myLabel = Label(root, text='Welcome to ID-CODE checker!').pack()    #label in program
myLabel2 = Label(root, text='Please input your ID-CODE').pack()    #label in program
user_entry = Entry(root, width=40, bg='black', fg='white', borderwidth=15)   # adding entry field, giving it colors and size
user_entry.pack()
# user_entry.insert(END, "Please input your ID_CODE: ") # if using insert, before is pack() command must be used as separate command, cannot use for user_entry =Entry().pack()



var = IntVar()
checkbox = Checkbutton(root, text='Check for validation', variable=var) # adding checkbox giving it name and addition information
# checkbox.deselect() # makes checkbox unselected as default
checkbox.pack() #calling checkbox

mybutton = Button(root, text='Check', padx=60, pady=10, command=Check, fg='black', bg='yellow')
mybutton.pack()




image1 = PhotoImage(file='domo.png')    # specifying picture file we want to use
mylabel = Label(root, image=image1).pack()  #calling image
# mylabel = Label(root, image=image1).grid(row=100, column=100)  #calling image , does not move the image......
quit_button = Button(root, text="Exit", padx=60, pady=10,  command=root.quit, fg='black', bg='red')  # quit button, root.quit is built in function
quit_button.pack()

print_output = StringVar()
output_label = Label(root, textvariable=print_output)
output_label.pack()


root.mainloop()
