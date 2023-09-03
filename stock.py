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

numeric = '1234567890'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='',
        db='stockmanagementsystem',
    )
    return conn

conn = connection()
cursor = conn.cursor()

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")
    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.pack()

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.connection.ping()
    cursor.execute("SELECT `item_id`,`name`,`price`,`quantity`,`category`,`date` FROM stocks ORDER BY `id` DESC")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def exportExcel():
    cursor.connection.ping()
    cursor.execute("SELECT `item_id`,`name`,`price`,`quantity`,`category`,`date` FROM stocks ORDER BY `id` DESC")
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
    messagebox.showinfo("", "Excel file downloaded")

placeholderArray = ['','','','','']

for i in range(0,5):
    placeholderArray[i] = tkinter.StringVar()

def setph(word,num):
    for ph in range(0,5):
        if ph == num:
            placeholderArray[ph].set(word)

def generateRand():
    itemId = ''
    for i in range(0,3):
        randno = random.randrange(0,(len(numeric)-1))
        itemId = itemId+str(numeric[randno])
    randno = random.randrange(0,(len(alpha)-1))
    itemId = itemId+'-'+str(alpha[randno])
    setph(itemId,0)
    print('generated: '+itemId)

def save():
    itemId = str(itemIdEntry.get())
    name = str(nameEntry.get())
    price = str(priceEntry.get())
    quantity = str(quantityEntry.get())
    cat = str(categoryCombo.get())
    valid = True
    if(not(itemId[3]=='-')):
        valid = False
    for i in range(0,3):
        if(not(itemId[i] in numeric)):
            valid = False
            break
    if(not(itemId[4] in alpha)):
        valid = False
    if not(valid):
        messagebox.showwarning("", "Invalid Item Id")
        return
    if (not(itemId and itemId.strip())) or (not(name and name.strip())) or (not(price and price.strip())) or (not(quantity and quantity.strip())) or (not(cat and cat.strip())):
        messagebox.showwarning("", "Please fill up all entries")
        return
    else:
        try:
            cursor.connection.ping()
            sql1=f"SELECT * FROM stocks WHERE `item_id` = '{itemId}' "
            cursor.execute(sql1)
            checkItemNo = cursor.fetchall()
            if len(checkItemNo) > 0:
                messagebox.showwarning("", "Item Id already used")
            else:
                cursor.connection.ping()
                sql2=f"INSERT INTO stocks (`item_id`, `name`, `price`, `quantity`, `category`) VALUES ('{itemId}','{name}','{price}','{quantity}','{cat}') "
                cursor.execute(sql2)
            conn.commit()
            conn.close()
        except:
            messagebox.showerror("", "Error while saving")
            return
    refreshTable()

def update():
    selectedItemid = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedItemid = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showwarning("", "Please select a data row")
        return

    print(selectedItemid) 
    itemId = str(itemIdEntry.get())
    name = str(nameEntry.get())
    price = str(priceEntry.get())
    quantity = str(quantityEntry.get())
    cat = str(categoryCombo.get())
    if (not(itemId and itemId.strip())) or (not(name and name.strip())) or (not(price and price.strip())) or (not(quantity and quantity.strip())) or (not(cat and cat.strip())):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    if(selectedItemid!=itemId):
        messagebox.showwarning("", "You can't change registed Item ID")
        return
    else:
        try:
            cursor.connection.ping()
            sql=f"UPDATE stocks SET `name` = '{name}', `price` = '{price}', `quantity` = '{quantity}', `category` = '{cat}' WHERE `item_id` = '{itemId}' "
            cursor.execute(sql)
            conn.commit()
            conn.close()
        except Exception as error:
            messagebox.showerror("", "Error occured reference: "+str(error))
            return

    refreshTable()

def delete():
    try:
        if(my_tree.selection()[0]):
            decision = messagebox.askquestion("", "Delete the selected data?")
            if decision != "yes":
                return 
            else:
                selected_item = my_tree.selection()[0]
                deleteData = str(my_tree.item(selected_item)['values'][0])
                try:
                    cursor.connection.ping()
                    sql = f"DELETE FROM stocks WHERE `item_id` = '{str(deleteData)}'"
                    cursor.execute(sql)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("", "Data has been successfully deleted")
                except:
                    messagebox.showinfo("", "Sorry, an error occured")
                    return
                refreshTable()
    except:
        messagebox.showwarning("", "Please select a data row")

def select():
    try:
        selected_item = my_tree.selection()[0]
        itemId = str(my_tree.item(selected_item)['values'][0])
        name = str(my_tree.item(selected_item)['values'][1])
        price = str(my_tree.item(selected_item)['values'][2])
        quantity = str(my_tree.item(selected_item)['values'][3])
        category = str(my_tree.item(selected_item)['values'][4])
        setph(itemId,0)
        setph(name,1)
        setph(price,2)
        setph(quantity,3)
        setph(category,4)
    except:
        messagebox.showwarning("", "Please select a data row")

def find():
    itemId = str(itemIdEntry.get())
    name = str(nameEntry.get())
    price = str(priceEntry.get())
    quantity = str(quantityEntry.get())
    category = str(categoryCombo.get())
    cursor.connection.ping()
    if(itemId and itemId.strip()):
        sql = f"SELECT `item_id`,`name`,`price`,`quantity`,`category` FROM stocks WHERE `item_id` LIKE '%{itemId}%' "
    elif(name and name.strip()):
        sql = f"SELECT `item_id`,`name`,`price`,`quantity`,`category` FROM stocks WHERE `name` LIKE '%{name}%' "
    elif(price and price.strip()):
        sql = f"SELECT `item_id`,`name`,`price`,`quantity`,`category` FROM stocks WHERE `price` LIKE '%{price}%' "
    elif(quantity and quantity.strip()):
        sql = f"SELECT `item_id`,`name`,`price`,`quantity`,`category` FROM stocks WHERE `quantity` LIKE '%{quantity}%' "
    elif(category and category.strip()):
        sql = f"SELECT `item_id`,`name`,`price`,`quantity`,`category` FROM stocks WHERE `category` LIKE '%{category}%' "
    else:
        messagebox.showwarning("", "Please fill up one on the entries")
        return
    cursor.execute(sql)
    try:
        result = cursor.fetchall()
        for num in range(0,5):
            setph(result[0][num],(num))
        conn.commit()
        conn.close()
    except:
        messagebox.showwarning("", "No data found")

def clear():
    for num in range(0,5):
        setph('',(num))

frame = tkinter.Frame(window, bg="#02577A")
frame.pack()

btnColor = '#196E78'

manageFrame= tkinter.LabelFrame(frame, text="Mange", borderwidth=5)
manageFrame.grid(row=0,column=0, sticky="w", padx=[10,200],pady=20,ipadx=[6])

saveBtn = Button(manageFrame, text="SAVE",width=10,borderwidth=3,bg=btnColor,fg='white',command=save)
saveBtn.grid(row=0,column=0,padx=5,pady=5)
updateBtn = Button(manageFrame, text="UPDATE",width=10,borderwidth=3,bg=btnColor,fg='white',command=update)
updateBtn.grid(row=0,column=1,padx=5,pady=5)
deleteBtn = Button(manageFrame, text="DELETE",width=10,borderwidth=3,bg=btnColor,fg='white',command=delete)
deleteBtn.grid(row=0,column=2,padx=5,pady=5)
selectBtn = Button(manageFrame, text="SELECT",width=10,borderwidth=3,bg=btnColor,fg='white',command=select)
selectBtn.grid(row=0,column=3,padx=5,pady=5)
findBtn = Button(manageFrame, text="FIND",width=10,borderwidth=3,bg=btnColor,fg='white',command=find)
findBtn.grid(row=0,column=4,padx=5,pady=5)
findBtn = Button(manageFrame, text="CLEAR",width=10,borderwidth=3,bg=btnColor,fg='white',command=clear)
findBtn.grid(row=0,column=5,padx=5,pady=5)
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
quantityLabel = Label(entriesFrame, text="QUANTITY",anchor="e",width=10)
quantityLabel.grid(row=3, column=0,padx=10)
categoryLabel = Label(entriesFrame, text="CATEGORY",anchor="e",width=10)
categoryLabel.grid(row=4, column=0,padx=10)

itemIdEntry = Entry(entriesFrame, width=50,textvariable = placeholderArray[0])
itemIdEntry.grid(row=0,column=2,padx=5,pady=5)
nameEntry = Entry(entriesFrame, width=50,textvariable = placeholderArray[1])
nameEntry.grid(row=1,column=2,padx=5,pady=5)
priceEntry = Entry(entriesFrame, width=50,textvariable = placeholderArray[2])
priceEntry.grid(row=2,column=2,padx=5,pady=5)
quantityEntry = Entry(entriesFrame, width=50,textvariable = placeholderArray[3])
quantityEntry.grid(row=3,column=2,padx=5,pady=5)
categoryCombo = ttk.Combobox(entriesFrame, values=['Networking Tools','Computer Parts','Repair Tools','Gadgets'], width=47,textvariable = placeholderArray[4])
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