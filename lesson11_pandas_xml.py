# import pandas as pd
# # df = pd.read_csv("2019.csv", header=1)
#
# pd.set_option("display.max_columns", 9)
# pd.set_option("display.max_rows", 157)

# print(df.head(10))    # if you write print(df.head(15)) we will get top 15

#________________________________________
# people = {
#     "first": ["Roman", "Bob", "John"],
#     "last": ["Kutselepa", "Smith", "Black"],
#     "email": ["roman@example.com", "oman@example.com", "man@example.com"]
# }
# df = pd.DataFrame(people)
# print(people["email"])
# print(df)
# print(df.email)  # or print(df["email"]) better to use one like this
#
# for x in df["email"]:  # or for x in df.email:
#     print(x)


#______________________________
import pandas as pd
df = pd.read_csv("2019.csv", header=1)
pd.set_option("display.max_columns", 9)
pd.set_option("display.max_rows", 157)
# print(df["Country or region"])    #will print one column
# print(df[["Country or region", "GDP per capita"]])  #will print two columns

# countries = list(df["Country or region"]) # will make all counties into list
# print(countries)
#iloc = "i" stands for integer(int)
# print(df.iloc[5])   # will print all data from 5 row
# print(df.iloc[5:16:2]) # will print from 5 index to 16 and each second line. -1 as third number will print backwards
# print(df.iloc[[0, 130 ,23, 37]])   # will print rows in such order as i gave 0, 130, 23, 37
# print(df.iloc[[0, 130 ,23, 37], [0, 1, 2]]) # first numbers are rows and  second numbers are number of column
# print(df.loc[[0, 130 ,23, 37], ["Country or region", "GDP per capita"]]) # if we use loc. then in as second we print names of columns, not numbers like in iloc
# print(df.loc[0, "Country or region"])   #we get name of country
#
# example
# df.loc[[y, y, y, y,], [x, x, x, x]]
# df.loc[[y, y, y, y,], x]


# for x in df.iloc[5]:    # will print each score separately in vertical
#     print(x)

# print(df.iloc[[0, 130 ,23, 37], [0, 1, 2]].shape)   # returns how mane numbers are used inside list = [4, 3]

# print(df["Country or region"].value_counts()) #counts how many times we find different countries, if counrty : finland is written 2 times we wil get finland 2, and those countries which are written more than once are printed at the beginning of the list
# print(df[["Score", "Country or region"]].value_counts())# will print list in ascending order using  score values
# print(df["Country or region"].value_counts(sort=False, ascending=True)) # will not sort like in previous and will return as ascending

# print(df.loc[[0, 120, 4, 7], "Country or region"].value_counts())
# print(df.loc[0:16, "Country or region" : "Freedom to make life choices"])

# print(df.columns)   # returns names of all columns
#
# pd.melt(df)
# print(df)
print(df.sort_values("Social support", ascending=False))   # returns and sorts in decreasing order
# print(df.sort_values("Social support")) #returns and sorts social support in increasing order
# # new_df = df.rename(columns={"Social support": "Hello World"}) # changes name of column
# new_df = df.rename(columns={"Social support": "Hello World", "Healthy life expectancy" : "Hello again"})   # replace names of two columns
# print(new_df)
#
# new_df = df[15:100] # returns with index from 15 to 100
# new_df = new_df.reset_index()   # resets previous line, and index will work like before from 0
# print(new_df)

# print(df[df["GDP per capita"] > 1]) # will return only those which are more than 1
# print(df.head(15)) #shows first 15 values
# print(df.tail(15)) # shows last 15 values


#______________________________XML
from xml.etree import ElementTree  # full name
# from xml.etree import ElementTree as et # shrotcut et

tree = ElementTree.parse("cd_catalog.xml")
root = tree.getroot()

# print(root)
# print(root.tag) #returns name of tag
# print(root.tag, root.attrib)    #returns name of tag and name of attribute
#
# for x in root:
#     print(x.tag, x.attrib)
#
# print(root[0][1].text) #takes cd 0 and first element from there == Bob Dylan, returns name of artist of the cd (takes cd1=artist)
# print(root[0][6][0].text) # takes cd1=sells=1 line

# print(root.iter("CD"))
#
# for element in root.iter("CD"):
#     print(element[0].text, element[1].text) # returns from CD root title[0] + name[0]


#
# for element in root.iter("SELLS"):
#     sold_albums = 0
#     for child in element:
#         sold_albums += int(child.text)
#     print(sold_albums)

cd = root[0]
data = next(cd.iter("Y1985"))
print(data.text)
data.text = str(int(data.text) + 100000) # adds 100000 to previous number
print(data.text)

tree.write("cd_catalog_copy.xml") # saves data.text = str(int(data.text) + 100000) into new file

#Homework = do program option choose what column is used and returns TOP15 ( if you can make user to choose TOPXX)