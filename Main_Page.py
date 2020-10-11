def new_acc():
    import Create_Account

def Login():
    import Login_Page


from tkinter import *

root = Tk()
root.title("Collage Bank")
root.geometry('720x380')
root.maxsize(720,380)
root.minsize(720,380)
root.config(bg='grey24')
# root.wm_iconbitmap("C:\Users\progr\Desktop\Bank\My_Codeing_world.ico")

Label(text="Welcome to College Bank\nNet Banking", font='Times 23 italic bold underline', fg='black', bg='DeepSkyBlue2', relief=RAISED, padx=50, pady=8).pack(anchor=N, pady=20, padx=100)

Label(justify=CENTER, text="College Bank is your college's new small commercial bank.Our bank\noffers range of general banking services from loans and advances\nto group and individuals", font='comicsansms 16', fg='black', bg='cyan', padx=10, pady=5).pack(anchor=N, pady=30, padx=20)



Frame_A = Frame(root, bg= 'White')
Label(Frame_A, text="For more queries contact on\nHelpline Number given below:-\n750XXXXX89", font="arial 12", padx=3, pady=3, justify=LEFT).pack(side=LEFT, anchor=W)
Frame_A.pack(side=LEFT, anchor=W, padx=40, pady=5)

Frame_B = Frame(root, bg="white")
Button(Frame_B, text="New Account", command=new_acc, padx=13, pady=2, font="Arial 13 bold", fg='black', bg='green').grid(row=0, pady=5, padx=4)
Button(Frame_B, text="Existing Account", command=Login, padx=0.8, pady=2, font="Arial 13 bold", fg='black', bg='green').grid(row=1, pady=5, padx=4)
Frame_B.pack(side=RIGHT, anchor=E, padx=50, pady=5)



root.mainloop()