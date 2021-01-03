from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

def generate():
    PasswordTextBox.config(state=NORMAL)
    password = ''
    if UpperCaseCheck.get()==0 and LowerCaseCheck.get()==0 and NumberCaseCheck.get()==0 and SpecialCharCaseCheck.get()==0:
        messagebox.showerror('Error','Select atleast one case') 
    else:
        if LengthTextBox.get()=='':
            messagebox.showerror('Error','please enter length')
        else:
            passwordlength = int(LengthTextBox.get())
        if UpperCaseCheck.get()!=0:
            uppercase = string.ascii_uppercase
        else:
            uppercase=''
        if LowerCaseCheck.get()!=0:
            lowercase = string.ascii_lowercase
        else:
            lowercase = ''
        if NumberCaseCheck.get()!=0:
            numbers = string.digits
        else:
            numbers = ''
        if SpecialCharCaseCheck.get()!=0:
            specialchar = string.punctuation
        else:
            specialchar = ''
        total_letters = lowercase+uppercase+numbers+specialchar
        for i in range(passwordlength):
            password = password+random.choice(total_letters)
        PasswordTextBox.delete(0,END)
        PasswordTextBox.insert(0,password)
        PasswordTextBox.configure(state='disabled')    

def copy_password():
    pyperclip.copy(PasswordTextBox.get())

def exit():
    PasswordGeneratorWindow.destroy()

PasswordGeneratorWindow = Tk()

PasswordGeneratorWindow.geometry('900x600+300+50')
PasswordGeneratorWindow.title('Password Generator')


HeadingLabel = Label(PasswordGeneratorWindow,text='Password generator',font=('arial',22,'bold'))
HeadingLabel.place(x=300,y=50)

UpperCaseCheck = IntVar()
UppercaseCheckButton = Checkbutton(PasswordGeneratorWindow,text='UpperCase(ABC)',onvalue=1,offvalue=0,variable=UpperCaseCheck,font=('arial',10))
UppercaseCheckButton.place(x=250,y=200)

LowerCaseCheck = IntVar()
LowercaseCheckButton = Checkbutton(PasswordGeneratorWindow,text='LowerCase(abc)',onvalue=1,offvalue=0,variable=LowerCaseCheck,font=('arial',10))
LowercaseCheckButton.place(x=250,y=150)

NumberCaseCheck = IntVar()
NumbercaseCheckButton = Checkbutton(PasswordGeneratorWindow,text='Numbers(123)',onvalue=1,offvalue=0,variable=NumberCaseCheck,font=('arial',10))
NumbercaseCheckButton.place(x=400,y=150)

SpecialCharCaseCheck = IntVar()
SpecialCharCheckButton = Checkbutton(PasswordGeneratorWindow,text='Special Characters($#&)',onvalue=1,offvalue=0,variable=SpecialCharCaseCheck,font=('arial',10))
SpecialCharCheckButton.place(x=400,y=200)

LengthLabel = Label(PasswordGeneratorWindow,text="Enter the length",font=("arial",12))
LengthLabel.place(x=200,y=250)
LengthTextBox = Entry(PasswordGeneratorWindow,font=('arial',16),bg='white')
LengthTextBox.place(x=350,y=250)

PasswordTextBox = Entry(PasswordGeneratorWindow,font=('arial',20),bg='lightgray',state='disabled')
PasswordTextBox.place(x=300,y=300)

GeneratePasswordButton = Button(PasswordGeneratorWindow,text="Generate Password",cursor='hand2',activebackground="green",bg="green",padx=10,pady=10,command=generate)
GeneratePasswordButton.place(x=250,y=380)

CopyPasswordButton = Button(PasswordGeneratorWindow,text="Copy to Clipboard",cursor='hand2',activebackground="green",bg="green",padx=10,pady=10,command=copy_password)
CopyPasswordButton.place(x=400,y=380)

ExitButton = Button(PasswordGeneratorWindow,text="Exit",cursor='hand2',activebackground="green",bg="green",padx=10,pady=10,command=exit)
ExitButton.place(x=550,y=380)

PasswordGeneratorWindow.mainloop()
