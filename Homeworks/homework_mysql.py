# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='Outrage39005110299',
#     database='homework'   # choosing database you will work with!
# )
#
# mycursor = mydb.cursor()
#
# def get_hospital_detail(hospital_id):
#     mycursor.execute("SELECT * FROM hospital")
#     myresult = mycursor.fetchall()  # returns only first line, with fetchall will return whole list.
#     for entry in myresult:
#         print(entry)
#
#
# def get_doctor_detail(doctor_id):
#     mycursor.execute("SELECT * FROM doctor")
#     myresult = mycursor.fetchall()
#     # print('Name = ' + str(myresult[1]))# returns only first line, with fetchall will return whole list.
#     for entry in myresult:
#         docid = entry[0]
#         name = entry[1]
#         hid = entry[2]
#         join = entry[3]
#         spec = entry[4]
#         salary = entry[5]
#         print('Printing Doctor record' + '\nDoctor Id:' + str(docid) + '\nDoctor Name:' + name +  '\nHospital Id:' + str(hid) + '\nJoining Date:' + str(join) + '\nSpeciality:' + spec
#               + '\nSalary:' + str(salary))
#
# get_doctor_detail(4)




#__________________________________________________________

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Outrage39005110299',
    database='homework'   # choosing database you will work with!
)

mycursor = mydb.cursor()
x = 1
def get_hospital_detail(hospital_id):
    df = pd.read_sql_query("SELECT * FROM hospital", mydb)
    print('Printing Hospital record' + '\nHospital Id:' + df.iloc[x][1])


def get_doctor_detail(doctor_id):
    mycursor.execute("SELECT * FROM doctor")
    myresult = mycursor.fetchall()
    # print('Name = ' + str(myresult[1]))# returns only first line, with fetchall will return whole list.
    for entry in myresult:
        docid = entry[0]
        name = entry[1]
        hid = entry[2]
        join = entry[3]
        spec = entry[4]
        salary = entry[5]
        print('Printing Doctor record' + '\nDoctor Id:' + str(docid) + '\nDoctor Name:' + name +  '\nHospital Id:' + str(hid) + '\nJoining Date:' + str(join) + '\nSpeciality:' + spec
              + '\nSalary:' + str(salary))

get_hospital_detail(1)