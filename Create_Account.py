# pip install tkcalendar

from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import SQLCommand
from tkinter import messagebox

def acc_create():
    if len(Name.get())>0 and len(father_name.get())>0 and len(Phone.get())==10 and len(address.get())>0:
        if len(Aadhar.get())==12:
            if Amount.get()>1000:
                Create = SQLCommand.CreateAccount(Name.get(), dob.get(), Phone.get(), Aadhar.get(), father_name.get(), address.get(), Amount.get(), password.get())
                messagebox.showinfo("Details", f"USer ID:\t{Aadhar.get()}\nPassword:{Create}")
                root.destroy()
            else:messagebox.showinfo("Error", 'You Opening Balance must be Greater Than 1000$')
        else:messagebox.showinfo("Error", 'Please Input Valid Aadhaar Number')
    else:messagebox.showinfo("Error", 'Sorry, Please fill All columns\nPerfectly')

root = Tk()
root.title("Sign Up To Bank Account")
root.geometry("500x470")
root.minsize(500,470)
root.maxsize(500, 470)
root.config(bg='grey24')
# root.wm_iconbitmap("C:\Users\progr\Desktop\Bank\My_Codeing_world.ico")

Label(root, text="Create Account At\nCollege Bank", font='Times 23 italic bold underline', padx=20, pady=5, fg='black', bg='DeepSkyBlue2', relief=RAISED).pack(anchor=N, side=TOP, padx=10, pady=10)


frame = Frame(root, bg='yellow2')


Label(frame, justify=LEFT, text="Enter Customer Name: ", font="comicsansms 13 bold", bg='yellow2', padx=5, pady=2).grid(row=0,column=0, pady=2)
Name = Entry(frame, font="comicsansms 11 italic")
Name.grid(row=0,column=1)


Label(frame, justify=LEFT,  text="Enter Aadhaar Number: ", font="comicsansms 13 bold", bg='yellow2', padx=5, pady=2).grid(row=1,column=0, pady=2)
Aadhar = Entry(frame, font="comicsansms 11 italic")
Aadhar.grid(row=1,column=1)


Label(frame, justify=LEFT,  text="Enter Date of Birth: ", font="comicsansms 13 bold", bg='yellow2', padx=5, pady=2).grid(row=2,column=0, pady=2)
dob = DateEntry(frame, width=18, bg="darkblue", fg="white", year=2002, month=5, day=19, font="comicsansms 11 italic")
dob.grid(row=2,column=1)



Label(frame, justify=LEFT,  text="Enter Father Name: ", font="comicsansms 13 bold", bg='yellow2', padx=5, pady=2).grid(row=3,column=0, pady=2)
father_name = Entry(frame, font="comicsansms 11 italic")
father_name.grid(row=3,column=1)



Label(frame, justify=LEFT,  text="Select gender: ", font="comicsansms 13 bold", bg='yellow2', padx=5, pady=2).grid(row=4, column=0, pady=2)
variable1 = StringVar()
gender = ttk.Combobox(frame, textvariable=variable1, state='readonly', width=24, height=5)
gender['values'] = ['Male', 'Female', 'Other']
gender.grid(row=4, column=1)


Label(frame,  justify=LEFT, text="Enter Phone Number: ", font="comicsansms 13 bold", bg='yellow2', padx=5, pady=2).grid(row=5,column=0, pady=2)
Phone = Entry(frame, font="comicsansms 11 italic")
Phone.grid(row=5,column=1)


Label(frame, justify=LEFT,  text="Enter address: ", font="comicsansms 13 bold", bg='yellow2', padx=5, pady=2).grid(row=6, column=0, pady=2)
address = Entry(frame, font="comicsansms 11 italic")
address.grid(row=6,column=1)


Label(frame, justify=LEFT,  text="Enter Password: ", font="comicsansms 13 bold", bg='yellow2', padx=5, pady=2).grid(row=7,column=0, pady=2)
password = Entry(frame, font="comicsansms 11 italic")
password.grid(row=7,column=1)

Label(frame, justify=LEFT,  text="Opening Balance:", font="comicsansms 13 bold bold", padx=5, pady=2, bg='red', fg='white').grid(row=8, column=0, pady=2)
Amount = Entry(frame, font="comicsansms 11 italic", bg='DarkSeaGreen1')
Amount.grid(row=8, column=1)


frame.pack(side=TOP, anchor=N, pady=10)

Button(root, text="Create Account", command=acc_create, font="comicsansms 16 bold", bg='green', fg='white', padx=17, pady=1, relief=SUNKEN).pack(side=TOP, anchor=N, fill=BOTH, padx=140, pady=10)




root.mainloop()
