#______Working with files  , when writing directories use // instead of /
# "r" - read
# "a" - append
# "w" - write
# "x" - create
# "r+" - read and write

# file = open("text.txt", "r", encoding="UTF8")   #UTF8 is language coding, better to use always
# print(file.name)    # returns name of file
# print(file.mode)    # returns mode that file is opened with
# print(file.closed)  # check if file open or closed, true if closed, false if file is open
#
# file.close()    # close file
# print(file.closed)


#______________ WITH      in that case after with python automatically closes the file, it is better to use in coding like this!
# with open("text.txt", "r", encoding="UTF8") as file:  # UTF8 is language coding, better to use always
#     print(file.name)  # returns name of file
#     print(file.mode)  # returns mode that file is opened with
#     print(file.closed)  # check if file open or closed, true if closed, false if file is open
#
# print(file.closed)

#___________________  file is read only once!
# with open("text.txt", "r", encoding="UTF8") as file:  # UTF8 is language coding, better to use always
#     data = file.readline() # reads only first line
#     # data = file.read() # returns text as type(str)
#     # data = file.readlines() # returns text as type(list), we can use it to read lines
#     print(data)
#     print(file.readline)

#__________________________________
# with open("text.txt", "r", encoding="UTF8") as file:
#     for line in file:
#         print(line, end="***")   # it adds *** at the end on each line, but in middle lines it will be before each line.

#______________________________
# with open("text.txt", "r", encoding="UTF8") as file:
#     # Number in () tells how many characters of the file to read
#     file_content = file.read(150)  # et wil read 150 symbols
#     print(file_content, end=" ")
#
#     file_content = file.read(150)  # now it will read next 150 symbols
#     print(file_content, end=" ")
#
#     file_content = file.read(150)  # now it will read next 150 symbols
#     print(file_content, end=" ")
#
#     file_content = file.read(150)  # now it will read next 150 symbols
#     print(file_content, end=" ")
#
#     file_content = file.read(150)  # now it will read next 150 symbols
#     print(file_content, end=" ")

#_______________________________    # read 100 symbols and adds *********************** at the end of each 100 symbols  and at the end of the text also
# with open("text.txt", "r", encoding="UTF8") as file:
#     size_to_read = 100
#     file_content = file.read(size_to_read)
#     while len(file_content) > 0:
#         print(file_content, end="******************")
#         file_content = file.read(size_to_read)

#____________________
# with open("text.txt", "r", encoding="UTF8") as file:
#     size_to_read = 100
#     file_content = file.read(size_to_read)
#     print(file_content)
#
#     file.seek(0)  # with that command he returns to the beginning of the text . file.seek(1000) - skips first 1000 symbols
#
#     file_content = file.read(size_to_read)
#     print(file_content)

#_____________________ WRITING FILES
with open("text2.txt", "w", encoding="UTF8") as file:

    # file.write('Test')
    # file.write("Test")
    file.write("Hello Oleg")  # he rewrites this text into the text each time you open

with open("text2.txt", "a", encoding="UTF8") as file:   # with command a(append) it will add new text to existing
    file.write(" ,Good Bye Oleg")




#opening pictures or files that are not txt. files .
# rb - reading byte
# wb - writing byte

#HOMEWORK - open file with big text and count number of words ( using split) and count unique words.  and write result to new file.
# (set and list to delete same words) and using replace delete ", ! . ?" and so on. find library to delete , ! ? .