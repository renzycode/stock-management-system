from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


root = Tk()
root.title("Stock Management System")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)

ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

myFontArray = ['Arial', 15]

label = Label(root, text="Stock Management System", font=(myFontArray))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

itemNoLabel = Label(root, text="Item No.",anchor="e",width=10, font=(myFontArray))

nameLabel = Label(root, text="Name",anchor="e",width=10, font=(myFontArray))
categoryLabel = Label(root, text="Category",anchor="e",width=10, font=(myFontArray))
priceLabel = Label(root, text="Price",anchor="e",width=10, font=(myFontArray))
quantityLabel = Label(root, text="Quantity",anchor="e",width=10, font=(myFontArray))

itemNoLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)

nameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
categoryLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
priceLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
quantityLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

itenNoEntry = Entry(root, width=40, bd=5, font=(myFontArray), state='disabled', textvariable = ph1)
generateNoBtn = Button(
    root, text="Generate No.", padx=20, pady=1, width=9,
    bd=5, font=(myFontArray), bg="#d7eeb4")

nameEntry = Entry(root, width=55, bd=5, font=(myFontArray), textvariable = ph2)
categoryEntry = Entry(root, width=55, bd=5, font=(myFontArray), textvariable = ph3)
priceEntry = Entry(root, width=55, bd=5, font=(myFontArray), textvariable = ph4)
quantityEntry = Entry(root, width=55, bd=5, font=(myFontArray), textvariable = ph5)

itenNoEntry.grid(row=3, column=1, columnspan=3, padx=5, pady=0)
generateNoBtn.grid(row=3, column=4, columnspan=1, rowspan=1)

nameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
categoryEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
priceEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
quantityEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Select", padx=50, pady=25, width=10,
    bd=5, font=(myFontArray), bg="#84F894")
updateBtn = Button(
    root, text="Find", padx=50, pady=25, width=10,
    bd=5, font=(myFontArray), bg="#84E8F8")
deleteBtn = Button(
    root, text="Save", padx=50, pady=25, width=10,
    bd=5, font=(myFontArray), bg="#FF9999")
searchBtn = Button(
    root, text="Update", padx=50, pady=25, width=10,
    bd=5, font=(myFontArray), bg="#F4FE82")
resetBtn = Button(
    root, text="Delete", padx=50, pady=25, width=10,
    bd=5, font=(myFontArray), bg="#F398FF")
selectBtn = Button(
    root, text="Reset", padx=50, pady=25, width=10,
    bd=5, font=(myFontArray), bg="#EEEEEE")

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=13, column=5, columnspan=1, rowspan=2)

root.mainloop()