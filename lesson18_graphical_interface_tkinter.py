# from tkinter import *   # * means we need to import all available classes from that library
#
# root = Tk() # name we are going to work with.
#
# user_entry = Entry(root,width=50, bg="black", fg='white', borderwidth=5)    # is used so user could input some text
# user_entry.pack()
# user_entry.insert(0, 'Please enter your name:  ') # adds this text to our input border
# user_entry.pack()
# def myClick():
#     my_label = Label(root, text=user_entry.get()) # returns text, that we have entered!
#     my_label.pack()
#
# root.title('This is Tkinter program!')  # gives name for root.mainloop window!
#
# root.geometry('920x640')    # we can change resolution of the window
#
# #____________Labels
# # my_label = Label(root, text='This is my first label')   # this label will be printed in our program window.
# # my_label.grid(row=0, column=2)
# #
# # my_label2 = Label(root, text='This is my second label')   # this label will be printed in our program window.
# # my_label2.grid(row=0, column=0)
# #
# # my_label2 = Label(root, text='This is my second label')   # this label will be printed in our program window.
# # my_label2.grid(row=2, column=2)
#
#
# #___________Button
# my_button = Button(root, text="Click me", command=myClick, fg='black', bg='red', padx=50, pady=10)   # text - button text, myClick must be defined, fg-front, bg-back color, padx and y size of button.
# my_button.pack()
#
#
# root.mainloop() # mainloop has to be always at the end of the program.



#________Program 2
from tkinter import *   # * means we need to import all available classes from that library

root = Tk() # name we are going to work with.
root.title('Squares calculator')
root.geometry('920x640')    # we can change resolution of the window



user_entry = Entry(root, width=35, borderwidth=5)
user_entry.grid(row=0, column=0, columnspan=3)
my_label = Label(root, text="Answer:")
my_label.grid(row=1, column=0)

display_text = StringVar()
def get_squares(number):
    user_entry.delete(0, END)   #will clear input windows from start to END!
    user_entry.insert(0, int(number) ** 2)  # will return that
    my_label = Label(root, text=user_entry.get())
    my_label.grid(row=1, column=0)
    #_____OR

    my_label = Label(root, text=int(number) ** 2)
    my_label.grid(row=1, column=0)



my_button = Button(root, text='Count squares', command=lambda: get_squares(user_entry.get()))   # we need to use lambda function to user get_squared function
my_button.grid(row=0, column=3)

my_label = Label(root, text=user_entry.get())
my_label.grid(row=1, column=0)


root.mainloop()