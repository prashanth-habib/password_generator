"""
This file contains the front end code for Password Generator App.
"""
from PasswordGenerator import PasswdGenerator
from tkinter import *


def pass_gen():
    passwd = PasswdGenerator()
    text = passwd.generate_passwd()
    entry1.delete(0, 'end')
    entry1.insert(0, text)


window = Tk()
window.title("password generator")
window.geometry("200x100")
window.resizable(False, False)

label1 = Label(window, text="password generator")
label1.pack(padx=5, pady=5)

entry1 = Entry(window)
entry1.pack(pady=5, padx=10)

gen_button = Button(window, text="get password", command=pass_gen)
gen_button.pack(pady=5, padx=5)
window.mainloop()
