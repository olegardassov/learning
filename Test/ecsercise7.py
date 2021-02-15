word = input("Please input your word to check it: ").replace(' ', "").lower()
if word == word[::-1]:
    print("OK")
else:
    print("NOK")
