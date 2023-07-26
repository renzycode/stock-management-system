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

MyFontArray = ['Arial', 15]

label = Label(root, text="Stock Management System", font=(MyFontArray))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

itemNoLabel = Label(root, text="Item No.",anchor="e",width=10, font=(MyFontArray))

nameLabel = Label(root, text="Name",anchor="e",width=10, font=(MyFontArray))
categoryLabel = Label(root, text="Category",anchor="e",width=10, font=(MyFontArray))
priceLabel = Label(root, text="Price",anchor="e",width=10, font=(MyFontArray))
quantityLabel = Label(root, text="Quantity",anchor="e",width=10, font=(MyFontArray))

itemNoLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)

nameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
categoryLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
priceLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
quantityLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

itenNoEntry = Entry(root, width=40, bd=5, font=(MyFontArray), textvariable = ph1)
generateNoBtn = Button(
    root, text="Generate No.", padx=20, pady=1, width=10,
    bd=5, font=(MyFontArray), bg="#84F894")

nameEntry = Entry(root, width=55, bd=5, font=(MyFontArray), textvariable = ph2)
categoryEntry = Entry(root, width=55, bd=5, font=(MyFontArray), textvariable = ph3)
priceEntry = Entry(root, width=55, bd=5, font=(MyFontArray), textvariable = ph4)
quantityEntry = Entry(root, width=55, bd=5, font=(MyFontArray), textvariable = ph5)

itenNoEntry.grid(row=3, column=1, columnspan=3, padx=5, pady=0)
generateNoBtn.grid(row=3, column=4, columnspan=1, rowspan=1)

nameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
categoryEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
priceEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
quantityEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

root.mainloop()