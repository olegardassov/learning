print("Hello, welcome to ID code verification system")
menu = input("Please choose 1 to input your ID code, choose 2 to verify your ID code or choose 0 to exit the program: ")
if menu == "1":
    id_code = input("Please input your ID_code here: ")
elif menu == "0":
    print("Thank you and see you next time. ")
    quit()
#ID code verification
elif menu == "2":
    id_code = input("Please input your ID_code here: ")
    control = 1 * int(id_code[0]) + 2 * int(id_code[1]) + 3 * int(id_code[2]) + 4 * int(id_code[3]) + 5 * int(id_code[4]) + 6 * int(id_code[5]) + 7 * int(id_code[6]) + 8 * int(id_code[7]) + 9 * int(id_code[8]) + 1 * int(id_code[9])
    # print(control)
    check = control % 11
    # print(check)
    if check < 10 and check == int(id_code[-1]):
        print("Code you entered is valid! ")
    else:
        control = 3 * int(id_code[0]) + 4 * int(id_code[1]) + 5 * int(id_code[2]) + 6 * int(id_code[3]) + 7 * int(id_code[4]) + 8 * int(id_code[5]) + 9 * int(id_code[6]) + 1 * int(id_code[7]) + 2 * int(id_code[8]) + 3 * int(id_code[9])
        # print(control)
        check = control % 11
        # print(check)
        if check < 10 and check == int(id_code[-1]):
            print("Code you entered is valid also!")
            if check >= 10:
                print('Your ID code control number is 0')
else:
    print("Oops, something went wrong. ")
    exit("Program stopped! ")
if  id_code.isdigit(): # with that command we can check if text inputed by user contains only digits
    print('Information you entered contains digits only! ')
else:
    print('Please use Digits only')
    exit('Program stopped!')
if len(id_code) == 11:
    print('Your id_code has been verified!')

elif len(id_code) < 11:
    print("Your id_code is too short!")
    exit("Program stopped!")
elif len(id_code) > 11:
    print("Your id_code is too long!")
    exit("Program stopped!")
if id_code[0:1] == "3" or id_code[0:1] == "1" or id_code[0:1] == "5" or id_code[0:1] == "7":
    print('Your gender is: Male')
elif id_code[0:1] == '4' or id_code[0:1] == '2' or id_code[0:1] == '6' or id_code[0:1] == '8':
    print('Your gender is: Female')
birthday = id_code[5:7] + "." +id_code[3:5] + "." + id_code[1:3]
print("Your birthday is: " + birthday)


if int(id_code[9:10]) >= 1 and int(id_code[8:10]) <= 10:
    print("Kuressaare haigla")

elif int(id_code[8:10]) >= 21 and int(id_code[7:10]) <= 150:
    print("Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja")

elif int(id_code[8:10]) >= 11 and int(id_code[8:10]) <= 19:
    print("Tartu Ülikooli Naistekliinik")

elif int(id_code[7:10]) >= 151 and int(id_code[7:10]) <= 160:
    print("Keila haigla")

elif int(id_code[7:10]) >= 161 and int(id_code[7:10]) <= 220:
    print("Rapla haigla, Loksa haigla, Hiiumaa haigla(Kärdla)")

elif int(id_code[7:10]) >= 221 and int(id_code[7:10]) <= 270:
    print("Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi")

elif int(id_code[7:10]) >= 271 and int(id_code[7:10]) <= 370:
    print("Maarjamõisa Kliinikum (Tartu), Jõgeva haigla")

elif int(id_code[7:10]) >= 371 and int(id_code[7:10]) <= 420:
    print("Narva haigla")

elif int(id_code[7:10]) >= 421 and int(id_code[7:10]) <= 470:
    print("Pärnu haigla")

elif int(id_code[7:10]) >= 471 and int(id_code[7:10]) <= 490:
    print("Haapsalu haigla")

elif int(id_code[7:10]) >= 491 and int(id_code[7:10]) <= 520:
    print("Järvamaa haigla, (Paide)")

elif int(id_code[7:10]) >= 521 and int(id_code[7:10]) <= 570:
    print("Rakvere haigla, Tapa haigla")

elif int(id_code[7:10]) >= 571 and int(id_code[7:10]) <= 600:
    print("Valga haigla")

elif int(id_code[7:10]) >= 601 and int(id_code[7:10]) <= 650:
    print("Viljandi haigla")

elif int(id_code[7:10]) >= 651 and int(id_code[7:10]) <= 700:
    print("Lõuna-Eesti haigla (Võru), Põlva haigla")
else:
    print("Oops, something went wrong! ")

print('Thank you for using our program! ')


