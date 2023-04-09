
from tkinter import *
from  tkinter import messagebox
from random import choice,randint,shuffle
import string
import pandas
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def ps_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    ps_letters=[choice(letters) for l in range(randint(6,8))]
    ps_symbols=[choice(symbols) for s in range(randint(2,4))]
    ps_numbers=[choice(numbers) for n in range(randint(2,4))]
    password_list= ps_letters+ps_numbers+ps_symbols
    shuffle(password_list)
    New_ps="".join(password_list)
    fill3.insert(0,New_ps)
    pyperclip.copy(New_ps)
# --------------------------- SAVE PASSWORD ------------------------------- #
def ps_list():
    a = fill1.get()
    b = fill2.get()
    c = fill3.get()

    if len(a)==0 or len(c)==0:
        messagebox.showwarning(title= "Warning",message="you Should fill all the boxes to continue")

    else:
        is_ok = messagebox.askokcancel(title=f"{a}",
                                       message=f"These are the details entered:\n  Email: {b}\n Password: {c}")
        if is_ok:
            with open("Save.txt","a") as data_file:
                data_file.write(f" {a} | {b} | {c}\n")
            fill1.delete(0,END)
            fill3.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("password manager")
window.config(padx=20, pady=20)
canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)
Add=Button(text="add",width=36,command=ps_list)
Add.grid(column=1,row=4,columnspan=2)
Generate=Button(text="Generate Password",command=ps_generator)
Generate.grid(column=2,row=3)
Web=Label(text="Website:")
Web.grid(column=0,row=1)
Email=Label(text="Email/username:")
Email.grid(column=0,row=2)
PS=Label(text="Password:")
PS.grid(column=0,row=3)
fill1=Entry(width=35)
fill1.grid(column=1,row=1,columnspan=2)
fill1.focus()
fill2=Entry(width=35)
fill2.grid(column=1,row=2,columnspan=2)
fill2.insert(0,"abyi@gmail.com")
fill3=Entry(width=21)
fill3.grid(column=1,row=3,)





window.mainloop()