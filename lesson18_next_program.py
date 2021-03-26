from tkinter import *

root = Tk()
root.title("Square")
root.geometry("920x640")



# root.iconbitmap("icon.ico") # can change icon
image1 = PhotoImage(file="python.png")

my_label = Label(root, image=image1)
my_label.pack()
# my_label.grid(row=10, column=10) # to choose where to put our pic. In case you use grid, you need to use grid everywhere. You cannot use .pack()

quit_button = Button(root, text="Exit", command=root.quit)  # quit button, root.quit is built in function
quit_button.pack()


root.mainloop()


# #__________VER2__ FRAME
# from tkinter import *
#
# root = Tk()
# root.title("Square")
# root.geometry("920x640")
#
# frame = LabelFrame(root, text='This is frame', padx=50, pady=50) # creates frame around button
# frame.pack(padx=10, pady=10)
#
# button = Button(frame, text='Click Me')
# button.pack()
#
# my_label = Label(frame, text='hello world') # using root or frame text will be inside or outside the frame
# my_label.pack()
#
# root.mainloop()


# #__________VER3__ FRAME
# from tkinter import *
#
# root = Tk()
# root.title("Square")
# root.geometry("920x640")
#
# frame = LabelFrame(root, text='This is frame', padx=50, pady=50) # creates frame around button
# frame.grid(row=0, column=3)
#
# button = Button(frame, text='Click Me')
# button.pack()
#
# my_label = Label(frame, text='hello world') # using root or frame text will be inside or outside the frame
# my_label.pack()
#
# root.mainloop()



# #__________RADIO BUTTON
# from tkinter import *
#
# root = Tk()
# root.title("Square")
# root.geometry("920x640")
#
# choice = IntVar()    # can be StringVar() or IntVar()
#
# choice.set('2') # is what is chosen as default
#
# def choice_done(value):
#     my_label = Label(root, text=value).pack()
#
# Radiobutton(root, text='Choice 1', variable=choice, value=1, command=lambda :choice_done(choice.get())).pack()
# Radiobutton(root, text='Choice 2', variable=choice, value=2, command=lambda :choice_done(choice.get())).pack()
# Radiobutton(root, text='Choice 3', variable=choice, value=3, command=lambda :choice_done(choice.get())).pack()
#
# my_label = Label(root, text=choice.get()).pack()
#
# root.mainloop()


# #__________RADIO BUTTON__VER2.
# from tkinter import *
#
# root = Tk()
# root.title("Square")
# root.geometry("920x640")
#
# modes = [
#     ('One', 'One'),
#     ('Two', 'Two'),
#     ('Three', 'Three'),
#     ('Four', 'Four')
# ]
#
# choice = StringVar()
# choice.set('One')
#
# for text, mode in modes:
#     Radiobutton(root, text=text, variable=choice, value=mode).pack()
#
# def choice_done(value):
#     my_label = Label(root, text=value).pack()
#     # display_text.set(value)
#
# display_text = StringVar()
# # my_label = Label(root, text=display_text).pack()
# my_button = Button(root, text="Click Me", command=lambda: choice_done(choice.get())).pack()
#
# root.mainloop()



# #__________CHECK_BOX
# from tkinter import *
#
# root = Tk()
# root.title("Square")
# root.geometry("920x640")
#
# def show_check_status():
#     my_lable = Label(root, text=var.get()).pack()
#
# var = StringVar()
# chk_box = Checkbutton(root, text='Check me', variable=var, onvalue='ON', offvalue='OFF')
# chk_box.deselect()  # if this is not used, check box will be selected as default, but pack() must be used after this command
# chk_box.pack()
#
# my_lable = Label(root, text=var.get()).pack()
#
# my_button = Button(root, text='Show check status', command=show_check_status).pack()
#
# root.mainloop()



# ____________MESSAGE_BOX
# from tkinter import *
# from tkinter import messagebox
#
# root = Tk()
# root.title("Square")
# root.geometry("920x640")
#
# def clicked():
#     response = messagebox.askyesnocancel('This is error message', 'This is a body of an error message')    # can be used showinfo, askquestion, showerror, showwarning,askyesnocancel,  gives new windows
#     Label(root, text=response).pack()
#     if response == 1:
#         Label(root, text='You clicked yes button').pack()
#     elif response == 0:
#         Label(root, text='You clicked no button').pack()
#     else:
#         Label(root, text='You clicked cancel').pack()
#
# Button(root, text='Click me', command=clicked).pack()
#
# root.mainloop()



#______________DROPDOWN MENU
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Square")
root.geometry("920x640")

def show():
    my_label = Label(root, text=dropdown.get()).pack()

menu_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
dropdown = StringVar()  # output is a string , not int
dropdown.set('Mon') # default value
# dropdown_menu = OptionMenu(root, dropdown, *menu_list).pack()
#OR
dropdown_menu = OptionMenu(root, dropdown, 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun').pack()


my_button = Button(root, text="Show selection", command=show).pack()

root.mainloop()

