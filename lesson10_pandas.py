# ##json
# import pandas as pd  # is is used to call library "pandas" as "pd"
# import json
#
# with open("sample2.json", "r", encoding="UTF8") as file:
#     data = json.load(file)
#
# df = pd.DataFrame(data["people"])   # we take out "people" from sample2.json file
# print(df)
# print(type(df))

##pandas

import pandas as pd
df = pd.read_csv("2019.csv", skiprows=1)   # with skiprows skips first row as we do not need it because it has keys to all inforamtion ( names of columns)
#OR
#df = pd.read_csv("2019.csv", header=1) # makes first line as a header
#df = pd.read_csv("2019.csv", header=None, name=["Overall rank" ,"Country or region","Score","GDP per capita","Social support","Healthy life expectancy","Freedom to make life choices","Generosity","Perceptions of corruption"])   # like that we can give names(header) for our columns
#df = pd.read_csv("2019.csv", header=1, rows=15)  # will show only 15 rows including header
print(df)  # doesnt show all columns and rows

pd.set_option("display.max_columns", 9)
pd.set_option("display.max_rows", 157)

print(df) # with two previous commands shows all rows and columns