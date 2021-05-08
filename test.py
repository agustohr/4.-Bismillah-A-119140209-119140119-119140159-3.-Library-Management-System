import mysql.connector as mysql
import os
from tabulate import tabulate

db = mysql.connect(
    host='localhost',
    user='root',
    password='',
    database='library_management_system'
)
def Library(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM library")
    myresult = mycursor.fetchall()

    print(tabulate(myresult, headers=["library_id","library_name"], tablefmt="grid"))

def Items(db):
    pilih = int(input("Library ID : "))
    mycursor = db.cursor()
    sql = "SELECT * FROM items WHERE library_id=%s"
    val = [pilih]
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()

    print(tabulate(myresult, headers=["item_id","library_id","category","title","author","publisher","production_year","copies"], tablefmt="grid"))

def Subscribers(db):
    print("Insert data subscriber\n")
    id_subs = input("Subscriber ID : ")
    tipe = input("Type : ")
    name = input("Name : ")
    address = input("Address : ")
    phone = input("Phone : ")
    email = input("Email : ")

    val = (id_subs, tipe, name, address, phone, email)
    mycursor = db.cursor()
    sql = "INSERT INTO subscribers (subscriber_id, type, name, address, phone, email) VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))

def Borrowing(db):
    print("Insert data borrowing\n")
    id_borrow = int(input("Borrowing ID : "))
    id_subs = int(input("Subscriber ID : "))
    borrow_date = input("Borrowing date : ")
    item_id = input("Item id : ")
    
    mycursor = db.cursor()
    val = (id_borrow, id_subs, item_id, borrow_date)
    sql = "INSERT INTO borrowing (borrowing_id, subscriber_id, item_id, borrow_date) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))

def Countdate(db):
    id_borrow = int(input("Borrowing ID : "))
    return_date = input("Returning date : ")
    mycursor = db.cursor()
    val = (return_date, id_borrow)
    sql = "UPDATE borrowing SET return_date = (%s) WHERE borrowing_id = (%s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))

    # sql = "SELECT datediff(return_date,borrow_date) FROM borrowing WHERE borrowing_id = (%s)
    # val = [pilih]
    # mycursor.execute(sql,val)
    # myresult = mycursor.fetchall()
    
    # if val == 'regular' :
    #     tgl1 = borrow_date.dd()
    #     tgl1 + 
    
    # elif val == 'golden' :

def Menu(db):
    print("=== Menu ===")
    print("1. Show Items")
    print("2. Register Subscriber")
    print("3. Borrowing")
    print("4. Keluar")
    pilih_menu = input("Pilih Menu : ")

    if pilih_menu == "1":
    	Library(db)
    	Items(db)
    elif pilih_menu == "2":
    	Subscribers(db)
    elif pilih_menu == "3":
        Borrowing(db)
        Countdate(db)
    elif pilih_menu == "4":
        exit()
    else:
        print("Menu Salah")

while(True):
	Menu(db)
