a = input('Please input a: ')
b = input('Please input b: ')
c = input('Please input c: ')
check = int(c) ** 2 == int(a) ** 2 + int(b) ** 2
if check == True:
    print("OK")
else:
    print("NOK")