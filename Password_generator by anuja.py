from tkinter import *
from random import randint

root =Tk()
root.title("Password Generator")
root.iconbitmap('')
root.geometry("500x500")

my_password = chr(randint(33,126))

def new_rand():
    pw_entry.delete(0,END)
    pw_length = int(my_entry.get())
    my_password=''
    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    pw_entry.insert(0,my_password)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

lf1= Label(root, text="-- Password Generator --" ,fg="blue", width=50, font=12)
lf1.pack(pady=10)

lf2= LabelFrame(root, text="Enter Username")
lf2.pack(pady=10)

my_entry1 =Entry(lf2, font=("Helvetica", 20),width=24)
my_entry1.pack(pady=20,padx=20)

lf = LabelFrame(root, text="How many Characters?")
lf.pack(pady=20)

my_entry =Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20,padx=20)

pw_entry= Entry(root, text='',font=("Helvetica", 24))
pw_entry.pack(pady=10)

my_frame=Frame(root)
my_frame.pack(pady=20)

my_button=Button(my_frame, text="Generate Password", command = new_rand, bg="brown", fg="white",font=10)
my_button.grid(row=0,column=0,padx=10,pady=10)

clip_button=Button(my_frame,text="Accept & Copy", command = clipper,bg="white")
clip_button.grid(row=4,column=0,padx=10)

root.mainloop()

