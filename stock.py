from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import random
import pymysql
import csv
from datetime import datetime
import numpy as np

window = tkinter.Tk()
window.title("Stock Management System")
my_tree = ttk.Treeview(window, show='headings', height=20)
window.geometry("720x640")
style = ttk.Style()



def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='',
        db='stockmanagement',
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
    for array in read():
        dateraw=array[5]
        print(array[5])
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")
    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.pack()

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT `item_id`,`name`,`price`,`qnt`,`category`,`date` FROM stocks ORDER BY `id` DESC")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def exportExcel():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT `item_id`,`name`,`price`,`qnt`,`category`,`date` FROM stocks ORDER BY `id` DESC")
    dataraw = cursor.fetchall()
    date = str(datetime.now());
    date = date.replace(' ', '_')
    date = date.replace(':', '-')   
    dateFinal = date[0:16]
    with open("stocks_"+dateFinal+".csv",'a',newline='') as f:
        w = csv.writer(f, dialect='excel')
        for record in dataraw:
            w.writerow(record)
    print("saved: stocks_"+dateFinal+".csv")
    conn.commit()
    conn.close()

placeholderArray = ['','','','','']

for i in range(0,5):
    placeholderArray[i] = tkinter.StringVar()

def setph(word,num):
    for ph in range(0,5):
        if ph == num:
            placeholderArray[ph].set(word)

numeric = '1234567890'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generateRand():
    itemId = ''
    for i in range(0,3):
        randno = random.randrange(0,(len(numeric)-1))
        itemId = itemId+str(numeric[randno])
    randno = random.randrange(0,(len(alpha)-1))
    itemId = itemId+'-'+str(alpha[randno])
    setph(itemId,0)
    print('generated: '+itemId)

def select():
    try:
        selected_item = my_tree.selection()[0]
        itemId = str(my_tree.item(selected_item)['values'][0])
        name = str(my_tree.item(selected_item)['values'][1])
        price = str(my_tree.item(selected_item)['values'][2])
        qnt = str(my_tree.item(selected_item)['values'][3])
        category = str(my_tree.item(selected_item)['values'][4])
        setph(itemId,0)
        setph(name,1)
        setph(price,2)
        setph(qnt,3)
        setph(category,4)
    except:
        messagebox.showwarning("", "Please select a data row")

def save():
    itemId = str(itemIdEntry.get())
    name = str(nameEntry.get())
    price = str(priceEntry.get())
    qnt = str(qntEntry.get())
    cat = str(categoryCombo.get())

    if (not(itemId and itemId.strip())) or (not(name and name.strip())) or (not(price and price.strip())) or (not(qnt and qnt.strip())) or (not(cat and cat.strip())):
        messagebox.showwarning("", "Please fill up all entries")
        return
    else:
        try:
            conn = connection()
            print(conn)
            cursor = conn.cursor()
            sql1=f"SELECT * FROM stocks WHERE `item_id` = '{itemId}' "
            cursor.execute(sql1)
            checkItemNo = cursor.fetchall()
            if len(checkItemNo) > 0:
                messagebox.showwarning("", "Item Id already used")
            else:
                sql2=f"INSERT INTO stocks (`item_id`, `name`, `price`, `qnt`, `category`) VALUES ('{itemId}','{name}','{price}','{qnt}','{cat}') "
                cursor.execute(sql2)

            conn.commit()
            conn.close()
        except:
            messagebox.showerror("", "Error while saving")
            return

    refreshTable()


frame = tkinter.Frame(window, bg="#02577A")
frame.pack()

manageFrame= tkinter.LabelFrame(frame, text="Mange", borderwidth=5)
manageFrame.grid(row=0,column=0, sticky="w", padx=[10,200],pady=20,ipadx=[52])

saveBtn = Button(manageFrame, text="SAVE",width=10,borderwidth=3,bg="#196E78",fg='white',command=save)
saveBtn.grid(row=0,column=0,padx=5,pady=5)
updateBtn = Button(manageFrame, text="UPDATE",width=10,borderwidth=3,bg="#196E78",fg='white')
updateBtn.grid(row=0,column=1,padx=5,pady=5)
deleteBtn = Button(manageFrame, text="DELETE",width=10,borderwidth=3,bg="#196E78",fg='white')
deleteBtn.grid(row=0,column=2,padx=5,pady=5)
selectBtn = Button(manageFrame, text="SELECT",width=10,borderwidth=3,bg="#196E78",fg='white',command=select)
selectBtn.grid(row=0,column=3,padx=5,pady=5)
findBtn = Button(manageFrame, text="FIND",width=10,borderwidth=3,bg="#196E78",fg='white')
findBtn.grid(row=0,column=4,padx=5,pady=5)

exportExcelBtn = Button(manageFrame, text="EXPORT EXCEL",width=15,borderwidth=3,bg="#196E78",fg='white',command=exportExcel)
exportExcelBtn.grid(row=0,column=6,padx=5,pady=5)

entriesFrame= tkinter.LabelFrame(frame, text="Form",borderwidth=5)
entriesFrame.grid(row=1,column=0,sticky="w", padx=[10,200],pady=[0,20],ipadx=[93])

itemIdLabel = Label(entriesFrame, text="ITEM ID",anchor="e",width=10)
itemIdLabel.grid(row=0, column=0,padx=10)
nameLabel = Label(entriesFrame, text="NAME",anchor="e",width=10)
nameLabel.grid(row=1, column=0,padx=10)
priceLabel = Label(entriesFrame, text="PRICE",anchor="e",width=10)
priceLabel.grid(row=2, column=0,padx=10)
qntLabel = Label(entriesFrame, text="QUANTITY",anchor="e",width=10)
qntLabel.grid(row=3, column=0,padx=10)
categoryLabel = Label(entriesFrame, text="CATEGORY",anchor="e",width=10)
categoryLabel.grid(row=4, column=0,padx=10)

itemIdEntry = Entry(entriesFrame, width=50,textvariable = placeholderArray[0])
itemIdEntry.grid(row=0,column=2,padx=5,pady=5)
nameEntry = Entry(entriesFrame, width=50,textvariable = placeholderArray[1])
nameEntry.grid(row=1,column=2,padx=5,pady=5)
priceEntry = Entry(entriesFrame, width=50,textvariable = placeholderArray[2])
priceEntry.grid(row=2,column=2,padx=5,pady=5)
qntEntry = Entry(entriesFrame, width=50,textvariable = placeholderArray[3])
qntEntry.grid(row=3,column=2,padx=5,pady=5)
categoryCombo = ttk.Combobox(entriesFrame, values=['Networking Tools','Computer Parts','Repair Tools'], width=47,textvariable = placeholderArray[4])
categoryCombo.grid(row=4,column=2,padx=5,pady=5)

generateIdBtn = Button(entriesFrame, text="GENERATE ID",borderwidth=3,command=generateRand)
generateIdBtn.grid(row=0,column=3,padx=5,pady=5)

style.configure(window)

my_tree['columns'] = ("Item Id","Name","Price","Quantity","Category","Date")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Item Id", anchor=W, width=70)
my_tree.column("Name", anchor=W, width=125)
my_tree.column("Price", anchor=W, width=125)
my_tree.column("Quantity", anchor=W, width=100)
my_tree.column("Category", anchor=W, width=150)
my_tree.column("Date", anchor=W, width=150)

my_tree.heading("Item Id", text="Item Id", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Price", text="Price", anchor=W)
my_tree.heading("Quantity", text="Quantity", anchor=W)
my_tree.heading("Category", text="Category", anchor=W)
my_tree.heading("Date", text="Date & Time Update", anchor=W)

my_tree.tag_configure('orow', background='#EEEEEE')
my_tree.pack()

refreshTable()

window.resizable(False, False) 
window.mainloop()