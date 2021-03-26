#terminal/cmd commands
#dir - returns all directories inside folder you are in.
#to open file - write its name like : main.py ( it must be inside your project)
#cd (choose directory) - we can choose another folde like :cd mylearning
# to move back : cd ../
# to move back and open another folder :cd ../mylearning
#help to get help for all commands
#mkdir (md) - make new directory, mkdir hello_world
#rmdir - delete directory (folder), rmdir hello_world


#pip commands
#pip help - returns all available commands for pip ( can be used for specific commands :pip help install)
#to downgrade library (example: pandas, newest is 1.2.3 ) :pip install pandas==1.2.2 ( will install version we choose)
#pip freeze - returns all installed libraries with their versions
#pip freeze > requirments.txt # returns you txt file with versions of all your installed libraries  (requirments is name defined by you, can be what ever you want).
#pip install -r requirments.txt # will install all needed libraries ( with needed versions) from requirments.txt file
#pip show pandas - returns all information about that library ,also shows if some other libraries depend on that library
#pip check pandas - to check if library works fine, and all files are present



#working with directories
import os
import pandas
import time

# print(dir(os))  # returns all available methods/commands for that library
# print(dir(pandas))  # returns all available methods/commands for that library
# print(os.getcwd())  # returns full path to directory we are in right now
#
# os.chdir('../') # goes back to previous folder
# print(os.getcwd())
# os.chdir('learning') # goes forward to learning folder  # when giving directories you need to use \\ instead of \ .
# print(os.getcwd())
#os.chdir('.\\test') . - means inside folder you are in at the moment

# print(os.listdir()) # returns all folder and files in our project in 0-9 , A-Z order (os.listdir())[0] can be indexed , folder do not have any extensions.

# os.makedirs('new_folder//sub_folder//test') # creates test folder inside sub_folder inside new_folder inside our project

# time.sleep(5)   # delays 5 second

# os.rmdir('new_folder/sub_folder/test')  # removes only last folder in directory in our case 'test'
# os.removedirs('new_folder/sub_folder/') # deletes all folders in directory
# os.rename('sample.txt', 'new.txt')    #renames sample.txt to new.txt can be used in drectories
# os.rename('file/sample.txt', 'new_file/new.txt')  # renaming file inside directories and directories as well

# print(os.stat('new.txt'))   # returns properties of the file , like right click on file and choose properties ,time is fromtimetotime (timestamp) format
# print(os.stat('new.txt').st_size)   # returns only size of the file
# print(os.stat('new.txt').st_ctime)  # returns only time when file was created in timestamp format!

# information = os.walk('C:/Users/Oleg/PycharmProjects/learning/')
# print(information)
# for dirpath, dirnames, filenames in information:    # will return dirpath, dirnames and filenames of all files inside project
#     print(f'Current path: {dirpath}')
#     print(f'Directory name :{dirnames}')
#     print(f'File name: {filenames}')
#


#________System Variables
# print(os.environ)   # returns already used system variables
# print(os.environ.get('HOMEPATH'))  # returns information about specified key is used for safety so noone who has your code , won,t see user and password of your email or etc.
# file_path = os.environ.get('HOMEPATH') + '\\new.txt'    # adds homepath to filename and gives you directory , for file we need \\ in front of file name.
# print(file_path)
# #OR
# file_path2 = os.path.join(os.environ.get('HOMEPATH'), 'new.txt')    # adds homepath to filename and gives you directory
# print(file_path2)
#
# print(os.path.basename('C:/Users/Oleg/PycharmProjects/learning/lesson17_libraries_directories_and_else.py')) # returns name of file, (even if such folder does not exist)
# print(os.path.dirname('C:/Users/Oleg/PycharmProjects/learning/lesson17_libraries_directories_and_else.py')) # returns path until last file/folder
# print(os.path.split("C:/Users/Oleg/PycharmProjects/learning/lesson17_libraries_directories_and_else.py")) # returns basename and dirname separately.
# print(os.path.exists("C:/Users/Oleg/PycharmProjects/learning/lesson17_libraries_directories_and_else.py"))  # returns boolean if file exists or not.
# print(os.path.isdir("C:/Users/Oleg/PycharmProjects/learning/lesson17_libraries_directories_and_else.py"))   #returns if such directory exists, returns false if such directory does not exist
# print(os.path.isfile('C:/Users/Oleg/PycharmProjects/learning/lesson17_libraries_directories_and_else.py'))  #returns if such file exists, is such file does not exist, returns False!
#
# print(os.path.splitext("C:/Users/Oleg/PycharmProjects/learning/lesson17_libraries_directories_and_else.py"))    # returns whole path and file extension separately
# file = os.path.splitext("C:/Users/Oleg/PycharmProjects/learning/lesson17_libraries_directories_and_else.py")    # checking if file is python file or not
# if file[1] == '.py':
#     print('Is python file')
# else:
#     print('Not python file')

# for item in os.listdir(): # returns all files
#     print(item)



# # #________ConfigParser
# from configparser import ConfigParser
#
# config = ConfigParser()
#
# config["EMAIL"] = {
#     'email': 'test@example.com',
#     'password': '12345678'
# }
#
# config['DATABASE'] = {
#     'name': 'DBNAME',
#     'password': '12345678',
#     'host': 'localhost'
# }
#
# config['DEFAULT'] = {
#     'login': 'mylogin',
#     'password': '12345678'
#
# }
#
# with open('config.ini', 'w') as configfile: # creates new file config.ini with all information ABOVE! if 'w' , each time will rewrite. if 'a' will add each time( might get copies)
#     config.write(configfile)


#_________VER2
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

# print(config.sections())    #returns names of bases, but does not return DEFAULT information
#
# print(list(config['EMAIL']))    # returns all keys in base 'EMAIL'
#
# password = config['EMAIL']['password']  # returns from base 'EMAIL' password: can be used for DEFAULT as well
# print(password)

config.add_section('NEWLOGIN')
config.set('NEWLOGIN', 'login', 'oleg123')
config.set('NEWLOGIN', 'password', '12345678')

with open('config.ini', 'a') as configfile:
    config.write(configfile)