#prasiddha basnet
#october 06 2024
#download the module name pybase 64
#import the GUI
#import thee message box
#import o
from tkinter import *
from tkinter import messagebox
import base64
import os
def decrpt():
    print("")

def encryption():
    password = code.get()
    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.config(bg="red")

        message = txt.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b16encode(encode_message)

        encrtpy = base64_bytes.decode("ascii")

        Label(screen1,text="Encrypt", font="arial 14", fg="white", bg="black").place(x=10, y=0)
        text2=Text(screen1, font="roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10,y=40,width=380, height=150)
        text2.insert(END, encryption)



#define a variable  name screen:
def Screen():
    global txt
    global code
    global screen
    #give a name to Call Tkinter as a Tk()
    screen = Tk()
    screen.title("encrypt and dycrypt")
    #375x398 is the size of the screen
    screen.geometry("375x398")
    #icon
    def reset():
        code.set("")
        txt.delete(1.0,END)
    Label(text="Enter the text for Encryption and decryption", fg="black", font=("arail, 10")).place(x=11, y=11)
    txt = Text(font="Robote, 20", background="white", relief=GROOVE, wrap=WORD, bd=0)
    txt.place(x=0, y=30, width=500, height=90)

    Label(text="Enter the secret key for Encryption and decryption", fg="black", font=("calibri, 11")).place(x=11, y=200)

    code = StringVar() #StringVar function in Tkinter as a way to store text variables and to edit text in widgets
    Entry(textvariable=code, width=19, bd=0, font=("arial, 25"), show="*"). place(x=5,y=250)

    #Buttons
    Button(text="ENCRYPTION",height=2, width=25, background="blue", fg="white",command=encryption).place(x=10,y=300)
    Button(text="DECRYPTION",height=2, width=25, background="green",command=decrpt).place(x=160,y=300)
    Button(text="RESET",height=2, width=40, background="red", bd=0,command=reset).place(x=30,y=350)

















    #title of the box
    #it's show the box
    screen.mainloop()

Screen()