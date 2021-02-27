word = input("Please input your word to check it: ").replace(' ', "").replace(",", "").lower()    # replace replaces space by nothing and lower make all inputed text into lower cases, we can use
if word == word[::-1]:
    print("OK")
else:
    print("NOK")

#if word.lower().replace(' ', "") == work.lower().replace(' ', "")[::-1]:     # wer can use also like that
#   print('OK')
#else:
#    print("NOK")