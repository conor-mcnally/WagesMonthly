from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog
import csv

def store():
    adate = date.get()
    aamount = amount.get()

    if(adate == None):
        print("Error with date")
        messagebox.showerror("Error", "There was an issue inputting the date")
    else:
        result = messagebox.askquestion("Submit", "You are about to enter the following data:\n" + "Date: " + str(adate) + "\nAmount: " + str(aamount))

        if(result == 'yes'):
            print('here')
            with open('workHours.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([adate, aamount])
            file.close()
        else:
            date.set("")
            amount.set("")

def clear_screen():
    date.set("")
    amount.set("")



#Set up frame
root = Tk()
root.config(background = "light grey")
root.geometry("500x300")

#Define all variables for GUI components
date = StringVar()
amount = DoubleVar()
#This is just so the default is not zero for easier entry
amount.set("")

#Row 0 heading
lblHeading = Label(root, text = "Enter pay packet details", font = ('Helvetica', 24, 'bold')).grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 10)

#Row 1 Components 
lblDate = Label(root, text = 'Date(dd.mm.yy)', font = ('Arial', 14, 'bold')).grid(row=1, column=1)
entryDate = Entry(root, textvariable= date, width=10).grid(row = 1, column = 2)

#Row 2 Components
lblAmount = Label(root, text = "Amount(£)", font=('Arial', 14, 'bold')).grid(row=2, column=1)
entryAmount = Entry(root, textvariable=amount, width=10).grid(row=2, column=2)

submit_button = Button(root, text = "Save", command=store ,bg='orange', fg='white').grid(row=4, column=1)
clear_button = Button(root, text = "Clear All", command = clear_screen, bg='orange', fg='white').grid(row=4, column=2)

root.mainloop()