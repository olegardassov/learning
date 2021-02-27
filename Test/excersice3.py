a = input('Please input a: ')
b = input('Please input b: ')
c = input('Please input c: ')
#or
#a, b, c = input('Please enter three sides of triangle separated by coma: ').split(", ")

if int(c) ** 2 == int(a) ** 2 + int(b) ** 2:
    print('OK')
else:
    print('NOK')

#or
#check = int(c) ** 2 == int(a) ** 2 + int(b) ** 2
# if check == True:
#     print("OK")
# else:
#     print("NOK")