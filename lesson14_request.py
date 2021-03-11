# https://xkcd.com/353/

import requests

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}  # must be used to check in you login using browser.

#___________________
# r = requests.get("https://xkcd.com/353/", timeout=3, headers=headers)
# print(r)
# print(dir(r))
# print(r.status_code)
# print(r.text)
# print(r.content)    # same as print(r.text) but more compact
#__________________________



# ERROR CODES
#200 success
#300 redirect
#400 client error
#500 server error

#________________
#
# r = requests.get("https://imgs.xkcd.com/comics/python.png", timeout=5)  # returns picture with that code
# with open("python.png", 'wb') as file:
#     file.write(r.content)

#_____________________

# r = requests.get("https://xkcd.com/353/", timeout=3, headers=headers)
# print(r.status_code)
# print(r.ok)


#___________________________
#
# r = requests.get("https://xkcd.com/353/", timeout=3)
# print(r.headers)    # you can check when was website last modified .

#___________________________ All new

# from bs4 import BeautifulSoup as BS
# import requests
#
# r = requests.get('https://gammatest.net/course/python/')
# soup = BS(r.content, 'html.parser')
# print(soup)
# print(soup.prettify())  # returns visually formatted html code
# print(soup.title)   # returns name of title
# print(soup.title.text)  # returns only text between two title tags

# match = soup.find("div", class_='col-md-12 col-sm-12')
# print(match.a)
# print(len(match))


#________________________
# match2 = soup.find_all("div", class_='col-md-12 col-sm-12')
# for item in match2:
#     print(item.a)
#     print(item.text)

#____________________________
# match2 = soup.findAll("div", class_='col-md-12 col-sm-12')




#_______________converter

from bs4 import BeautifulSoup as BS
import requests


def user_choice():
    try:
        user_input = input("Please choose:\n1. Convert RUB to EUR\n2. Convert EUR to RUB\n3. Exit\n-->")

        if user_input == '1':
            amount = float(input("Please enter amount:\n-->"))
            result = amount * get_currency_value()
            print(result, "EURO")
        elif user_input == "2":
            amount = float(input("Please enter amount:\n-->"))
            result = amount / get_currency_value()
            result_string = "{result:.2f} Rubles"
            print(result_string.format(result=result))
        elif user_input == '3':
            print("Exit")
        else:
            print("Choice is out of range")
            user_choice()
    except:
        print("Error")
        user_choice()

def get_currency_value():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    url = "https://www.google.com/search?sxsrf=ALeKk01s3bPyqGpVBpjnzUKmTJNSbeTnng%3A1615398143365&source=hp&ei=_wRJYKPqE865kgXfsYiIAQ&iflsig=AINFCbYAAAAAYEkTDyXYXJB-oTcg3EU5LKaHkWD68w38&q=rub+to+eur&oq=rub+to+eur&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjIFCAAQywEyAggAMgIIADIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLAToECCMQJzoICAAQxwEQrwE6AgguOgQIABAKUNMBWPEIYPkLaABwAHgAgAHOAYgBgweSAQU3LjEuMZgBAKABAaoBB2d3cy13aXo&sclient=gws-wiz&ved=0ahUKEwjj5YOEo6bvAhXOnKQKHd8YAhEQ4dUDCAc&uact=5"
    full_page = requests.get(url, timeout=5, headers=headers)
    # print(full_page)    # to check if we get response from site
    soup = BS(full_page.content, "html.parser")
    # print(soup.prettify())  #returns visually converted html code
    currency_value = soup.findAll("span", {'class': "DFlfde SwHCTb"})   # if one class, can be used ("span", class_= "DFlfde SwHCTb")
    result = currency_value[0].text.replace(',', '.')
    return float(result)


user_choice()


