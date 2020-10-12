from tkinter import *
from datetime import datetime


def start_transaction(aadhar, Amount):
    
    def credit():
        val = int(value.get())
        from SQLCommand import transaction as tracn
        with open(f"PassBooks\\{aadhar}.txt", 'a+') as file:
            file.write(f"\nAt Date-Time: {datetime.now()}\t\tAmount credited: {val}")
            file.write(f"\n\t\tCurrent Balance:{Amount + val}")
        tracn(aadhar, Amount + val)

    def debit():
        val = int(value.get())
        from SQLCommand import transaction as tracn
        if Amount - val > 10:
            with open(f"PassBooks\\{aadhar}.txt", 'a+') as file:
                file.write(f"\nAt Date-Time: {datetime.now()}\t\tAmount debited: {val}")
                file.write(f"\n\t\tCurrent Balance:{Amount - val}")
            tracn(aadhar, Amount - val)
        else:
            pass
    
    
    root = Tk()
    root.title("Collage Bank")
    root.geometry('530x330')
    root.maxsize(530, 330)
    root.minsize(530, 330)
    root.config(bg='silver')
    root.config(bg="grey24")
    # root.wm_iconbitmap("C:\Users\progr\Desktop\Bank\My_Codeing_world.ico")

    Label(root, text="Welcome to College Bank\nNet Banking", font='Times 23 italic bold underline', fg='black', bg='DeepSkyBlue2', relief=RAISED, padx=50, pady=8).pack(anchor=N, pady=20, padx=20)

    Frame1 = Frame(root, bg='yellow2')
    Label(Frame1, text="Account Number: ", padx=16, pady=2, font='arial 12 bold', bg='yellow2').grid(row=0, column=0)
    Label(Frame1, text=aadhar, padx=16, pady=2, font='arial 12 bold', bg='yellow2').grid(row=0, column=1, padx=3, pady=2)

    Label(Frame1, text="Transaction Amount: ", padx=5, pady=2, font='arial 12 bold', bg='yellow2').grid(row=1, column=0)
    value = Entry(Frame1, font='arial 10')
    value.grid(row=1, column=1, padx=5, pady=6)
    Frame1.pack(pady=15, side=TOP)

    Frame_B = Frame(root, bg="white")
    Button(Frame_B, text="Credit Amount", command=credit, padx=3, pady=2, font="Arial 13 bold", fg='black',
           bg='green').grid(row=0)
    Button(Frame_B, text="Debit Amount", command=debit, padx=3, pady=2, font="Arial 13 bold", fg='black',
           bg='green').grid(row=1)
    Frame_B.pack(side=TOP, anchor=N, padx=70, pady=10)

    root.mainloop()
    
    
