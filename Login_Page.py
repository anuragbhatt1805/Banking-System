def Login():
    from SQLCommand import loginAccount
    loginAccount(User_ID.get(), Password.get())
    root.destroy()
 

from tkinter import *

root = Tk()
root.title("Collage Bank")
root.geometry('300x300')
root.minsize(300, 300)
root.maxsize(300, 300)
root.config(bg='grey24')
# root.wm_iconbitmap("C:\Users\progr\Desktop\Bank\My_Codeing_world.ico")

Label(root, text="Login to\nCollege Bank", font='Times 23 italic bold underline', fg='black', bg='DeepSkyBlue2', relief=RAISED, padx=50, pady=3).pack(side=TOP, anchor=N, pady=20, padx=20)

Frame1 = Frame(root, bg='yellow2')
Label(Frame1, text="User Id: ", padx=16, pady=2, font='arial 12 bold', bg='yellow2').grid(row=0, column=0)
User_ID = Entry(Frame1, font='arial 10')
User_ID.grid(row=0, column=2, padx=5, pady=6)

Label(Frame1, text="Password: ", padx=5, pady=2, font='arial 12 bold', bg='yellow2').grid(row=1, column=0)
Password = Entry(Frame1, show='*', font='arial 10')
Password.grid(row=1, column=2, padx=5, pady=6)
Frame1.pack(pady=15, side=TOP)

Button(root, text="Submit/Login", command=Login, padx=13, pady=2, font="Arial 13 bold", fg='black', bg='green').pack(pady=20, padx=80, side=TOP, anchor=N)


root.mainloop()