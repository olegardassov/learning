import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Outrage39005110299',
    database='testdb'   # choosing database you will work with!
)

# print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE testdb")  #base with that name can be created only once.

#___________________________________________________

# mycursor.execute('SHOW DATABASES')  # will return whole list of databases you have!
# for db in mycursor:
#     print(db)
#     print(db[0])    # will return names as string

# mycursor.execute('CREATE TABLE students (name VARCHAR(255), age INTEGER(10))')    #can be used only once

#____________________________________________________

# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table[0]) #returns name of table

#__________________________________________________________

# student1 = ("John", 32)
# student2 = [("John", 32), ("Roman", 36), ("Jane", 41)]
# name = "Mary"
# age = 25

#mycursor.execute('INSERT INTO students (name, age) VALUES ("Jack", 40)')
#OR
# mycursor.execute('INSERT INTO students (name, age) VALUES ("' + name + '", ' + str(age) + ')')


# sqlquery = 'INSERT INTO students (name, age) VALUES (%s, %s)'
# # mycursor.execute(sqlquery, student1)    # will add student1 to our table.
#
#
# mycursor.executemany(sqlquery, student2)    # will add whole list from student2
#
# mydb.commit()



#_____________________________________


# mycursor.execute("SELECT * FROM students")
# myresult = mycursor.fetchall()
# print(myresult)
# print(myresult[0])  # will return first from list to return only Name print(myresult[0][0])
# #OR
# for student in myresult:
#     print(student)
#     print("Hello " + student[0] + '.You are ' + str(student[1]) + ' years old.')

#____________________________________
# mycursor.execute("SELECT * FROM students")
# myresult = mycursor.fetchone()
# print(myresult)
# myresult = mycursor.fetchone()  # each next time returns next information from table
# print(myresult)
#
#
# while myresult != None:
#     print(myresult)
#     myresult = mycursor.fetchone()  # will return whole list

#____________________________________
# mycursor.execute("SELECT * FROM students")
# myresult = mycursor.fetchone()  # returns only first line, with fetchall will return whole list.
# for entry in myresult:
#     print(entry)

#____________________________
# sqlformula = "SELECT * FROM students WHERE name = %s"   #%s means it is variable
# mycursor.execute(sqlformula, ("Roman",)) # must be written like that, or you will get error
# myresult = mycursor.fetchall()
# for res in myresult:
#     print(res)
#
# sqlformula = "SELECT * FROM students WHERE age > %s"   #%s means it is variable
# mycursor.execute(sqlformula, ("30",)) # must be written like that, or you will get error
# myresult = mycursor.fetchall()
# for res in myresult:
#     print(res)



#__________PANDAS

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Outrage39005110299',
    database='testdb'   # choosing database you will work with!
)
x = 5
df = pd.read_sql_query("SELECT * FROM students", mydb)
print(df.iloc[x][0])