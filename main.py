import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import random


root = Tk()
root.title("Stock Management System")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)

myFontArray = ['Arial', 15]

def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='',
        db='stocks_db',
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=(myFontArray))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT `item_no`, `name`, `category`, `price`, `quantity` FROM stocks")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

#placeholder set value function
def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)

alphanumeric = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def generateRand():

    itemNo = ''

    for i in range(0,7):
        randno = random.randrange(0,(len(alphanumeric)-1))
        itemNo = itemNo+str(alphanumeric[randno])

    setph(itemNo,1)
    print(itemNo)

def select():
    try:
        selected_item = my_tree.selection()[0]
        itemno = str(my_tree.item(selected_item)['values'][0])
        name = str(my_tree.item(selected_item)['values'][1])
        category = str(my_tree.item(selected_item)['values'][2])
        price = str(my_tree.item(selected_item)['values'][3])
        quantity = str(my_tree.item(selected_item)['values'][4])

        setph(itemno,1)
        setph(name,2)
        setph(category,3)
        setph(price,4)
        setph(quantity,5)
    except:
        messagebox.showinfo("Error", "Please select a data row")

def save():
    itemno = str(itemNoEntry.get())
    name = str(nameEntry.get())
    category = str(categoryEntry.get())
    price = str(priceEntry.get())
    quantity = str(quantityEntry.get())

    if (itemno == "" or itemno == " ") or (name == "" or name == " ") or (category == "" or category == " ") or (price == "" or price == " ") or (quantity == "" or quantity == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            sql1 = f"SELECT * FROM stocks WHERE `item_no` = '{itemno}' "
            cursor.execute(sql1)
            checkItemNo = cursor.fetchall()
            if len(checkItemNo) > 0:
                print('existing'+checkItemNo)
            else:
                sql2 = f"INSERT INTO stocks (`item_no`, `name`, `category`, `price`, `quantity`) VALUES ('{itemno}','{name}','{category}','{price}','{quantity}') "
                cursor.execute(sql2)

            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Item No already exist")
            return

    refreshTable()

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

itemNoEntry = Entry(root, width=40, bd=5, font=(myFontArray), state='disabled', textvariable = ph1)
generateNoBtn = Button(
    root, text="Generate No.", padx=20, pady=1, width=9,
    bd=5, font=(myFontArray), bg="#d7eeb4", command=generateRand)

nameEntry = Entry(root, width=55, bd=5, font=(myFontArray), textvariable = ph2)
categoryEntry = Entry(root, width=55, bd=5, font=(myFontArray), textvariable = ph3)
priceEntry = Entry(root, width=55, bd=5, font=(myFontArray), textvariable = ph4)
quantityEntry = Entry(root, width=55, bd=5, font=(myFontArray), textvariable = ph5)

itemNoEntry.grid(row=3, column=1, columnspan=3, padx=5, pady=0)
generateNoBtn.grid(row=3, column=4, columnspan=1, rowspan=1)

nameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
categoryEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
priceEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
quantityEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

selectBtn = Button(
    root, text="Select", padx=50, pady=25, width=5,
    bd=5, font=(myFontArray), bg="#84F894", command=select)
findBtn = Button(
    root, text="Find", padx=50, pady=25, width=5,
    bd=5, font=(myFontArray), bg="#84E8F8")
saveBtn = Button(
    root, text="Save", padx=50, pady=25, width=5,
    bd=5, font=(myFontArray), bg="#FF9999", command=save)
updateBtn = Button(
    root, text="Update", padx=50, pady=25, width=5,
    bd=5, font=(myFontArray), bg="#F4FE82")
deleteBtn = Button(
    root, text="Delete", padx=50, pady=25, width=5,
    bd=5, font=(myFontArray), bg="#F398FF")
resetBtn = Button(
    root, text="Reset", padx=50, pady=25, width=5,
    bd=5, font=(myFontArray), bg="#EEEEEE")

selectBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
findBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
saveBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=13, column=5, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=(myFontArray))

my_tree['columns'] = ("Item No.","Name","Category","Price","Quantity")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Item No.", anchor=W, width=170)
my_tree.column("Name", anchor=W, width=150)
my_tree.column("Category", anchor=W, width=150)
my_tree.column("Price", anchor=W, width=165)
my_tree.column("Quantity", anchor=W, width=150)

my_tree.heading("Item No.", text="Item No.", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Category", text="Category", anchor=W)
my_tree.heading("Price", text="Price", anchor=W)
my_tree.heading("Quantity", text="Quantity", anchor=W)

refreshTable()

root.mainloop()