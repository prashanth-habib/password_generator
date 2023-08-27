"""
This file contains the front end code for Password Generator App.
"""
from PasswordGenerator import PasswdGenerator
from tkinter import *
passwd = PasswdGenerator()


def pass_gen():
    text = passwd.generate_passwd()
    entry1.delete(0, 'end')
    entry1.insert(0, text)


def set_passwd_length():
    current_length = entry2.get()
    passwd.set_length(int(current_length))
    new_length = passwd.passwd_length
    entry2.delete(0, 'end')
    entry2.insert(0, new_length)



window = Tk()
window.title("password generator")
window.geometry("300x200")
window.resizable(False, False)

label1 = Label(window, text="password generator")
label1.pack(padx=5, pady=5)

entry1 = Entry(window)
entry1.pack(pady=5, padx=10)

gen_button = Button(window, text="get password", command=pass_gen)
gen_button.pack(pady=5, padx=5)

entry2 = Entry(window)
entry2.insert(0, passwd.passwd_length)
entry2.pack(padx=5, pady=5)

set_len_button = Button(window, text="set length", command=set_passwd_length)
set_len_button.pack(pady=5, padx=5)

window.mainloop()
