import pandas as pd
df = pd.read_csv("2019.csv", header=1)
pd.set_option("display.max_columns", 9)


try:
    user_choice = input(
        "Please choose Column to use as a filter: \n1. Score \n2. GDP per capita \n3. Social support \n4. Healthy life expectancy \n5. Freedom to make life choices \n6. Generosity \n7. Perceptions of corruption \n-->: ")
    val = int(user_choice)
    top = input("Please input how long should your TOP be: ")
    val2 = int(top)
    filter = input("Please input, if ascedning should be  true or false: ").lower()
    if filter == "true":
        y = True
    elif filter == "false":
        y = False
    else:
        print("Your text is not true or false")
        quit()
except ValueError:
    print("That's not an int!")
    quit('Program has stopped')
# y = bool(filter)
print(filter)
x = int(top) + 1
if user_choice == '1':
    print(df.sort_values(by=["Score"], ascending=y).head(x))
elif user_choice == '2':
    print(df.sort_values(by=["GDP per capita"], ascending=y).head(x))
elif user_choice == '3':
    print(df.sort_values(by=["Social support"], ascending=y).head(x))
elif user_choice == '4':
    print(df.sort_values(by=["Healthy life expectancy"], ascending=y).head(x))
elif user_choice == '5':
    print(df.sort_values(by=['Freedom to make life choices'], ascending=y).head(x))
elif user_choice == '6':
    print(df.sort_values(by=["Generosity"], ascending=y).head(x))
elif user_choice == '7':
    print(df.sort_values(by=["Perceptions of corruption"], ascending=y).head(x))
else:
    print("Oops, something went wrong")


    # print(df.iloc[[0, 1 ,2 ,3], [0, 1, 2]])
    # print(df.loc[0:16, 'Overall rank': "Freedom to make life choices"].value_counts(sort=True, ascending=True))
    # print(df["Score"].value_counts(sort=True, ascending=True))
    # print(df['Overall rank': 'Country or region': "Score"].value_counts(sort=False, ascending=True))











# df.sort_values(by=["Score"], inplace=True)
# print(df)