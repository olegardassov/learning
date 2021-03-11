from bs4 import BeautifulSoup as BS
import requests
state = True
print("Hello!")

def user_choice():
    try:
        user_input = input("Please choose:\n1. Random facts\n2. Exit\n-->")
        if user_input == "1":
            print(random_facts())
            try:
                while state == True:
                    user_input2 = input("Please choose:\n1. For next Random fact\n2. Exit\n-->")
                    if user_input2 == '1':
                        print(random_facts())
                    elif user_input2 == '2':
                        state == False
                        print('Exit')
                        print("Good Bye")
                        break
                    else:
                        print("Choice is out of range")
                        user_choice()
            except:
                print("ERROR")
                user_choice()
        elif user_input == "2":
            print("Exit")
            print("Good Bye")
        else:
            print("Choice is out of range")
            user_choice()
    except:
        print("ERROR")
        user_choice()

def random_facts():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    url = ('https://www.google.com/search?sxsrf=ALeKk0166IkvmbseXYxTODiAyCaAxjB3IQ%3A1615469743975&source=hp&ei=rxxKYIbMOZiCjLsP4b-78AE&iflsig=AINFCbYAAAAAYEoqvznl_gPrC3uRgn2U7iu7C4Jv50UU&q=random+facts&oq=random+facts&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBOgUILhCTAjoICAAQxwEQowI6AggAOgQIIxAnOggIABDHARCvAToCCC5QmIcEWMKTBGCRlQRoAHAAeACAAbIBiAGpCJIBBDEwLjKYAQCgAQGqAQdnd3Mtd2l6&sclient=gws-wiz&ved=0ahUKEwjG3-7hrajvAhUYAWMBHeHfDh4Q4dUDCAc&uact=5')
    full_page = requests.get(url, timeout=10, headers=headers)
    # print(full_page.status_code)
    soup = BS(full_page.content, 'html.parser')
    # print(soup.title.value)
    question = soup.findAll('div', {'class' : "sW6dbe"})
    answer = soup.findAll('div', class_= 'DRBylb')
    result1 = question[0].text
    result2 = answer[0].text
    print('Random Fact!')
    print('Question:' + result1)
    print('Answer:' + result2)

user_choice()

