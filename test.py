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
        pass
    elif pilih_menu == "4":
        exit()
    else:
        print("Menu Salah")

while(True):
	Menu(db)
