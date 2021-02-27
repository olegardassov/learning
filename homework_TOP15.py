import pandas as pd
df = pd.read_csv("2019.csv", header=1)
pd.set_option("display.max_columns", 10)

while True:
    try: # checks if entered value is a number
        user_choice = input(
            "Please choose Column to use as a filter: \n1. Score \n2. GDP per capita \n3. Social support \n4. Healthy life expectancy \n5. Freedom to make life choices \n6. Generosity \n7. Perceptions of corruption \n-->: ")
        val = int(user_choice)
        top = input("Please input how long should your TOP be: ")
        val2 = int(top)
        filter = input("Please input, if ascedning should be  true or false: ").lower()
        if filter == "true":
            y = True
            break
        elif filter == "false":
            y = False
            break
        else:
            print("ERROR. Please try again! ")
    except ValueError:
        print("That is not a number.")
print(filter)
x = int(top)
if user_choice == '1':
    new = df.sort_values(by=["Score"], ascending=y).head(x)
    print(df.sort_values(by=["Score"], ascending=y).head(x)), new.to_csv("result.csv", index=True) # saves output to "result.csv" file
elif user_choice == '2':
    new = df.sort_values(by=["GDP per capita"], ascending=y).head(x)
    print(df.sort_values(by=["GDP per capita"], ascending=y).head(x)), new.to_csv("result.csv")
elif user_choice == '3':
    new = df.sort_values(by=["Social support"], ascending=y).head(x)
    print(df.sort_values(by=["Social support"], ascending=y).head(x)), new.to_csv("result.csv")
elif user_choice == '4':
    new = df.sort_values(by=["Healthy life expectancy"], ascending=y).head(x)
    print(df.sort_values(by=["Healthy life expectancy"], ascending=y).head(x)), new.to_csv("result.csv")
elif user_choice == '5':
    new = df.sort_values(by=['Freedom to make life choices'], ascending=y).head(x)
    print(df.sort_values(by=['Freedom to make life choices'], ascending=y).head(x)), new.to_csv("result.csv")
elif user_choice == '6':
    new = df.sort_values(by=["Generosity"], ascending=y).head(x)
    print(df.sort_values(by=["Generosity"], ascending=y).head(x)), new.to_csv("result.csv")
elif user_choice == '7':
    new = df.sort_values(by=["Perceptions of corruption"], ascending=y).head(x)
    print(df.sort_values(by=["Perceptions of corruption"], ascending=y).head(x)), new.to_csv("result.csv")
else:
    print("Number you entered is out of range!")


