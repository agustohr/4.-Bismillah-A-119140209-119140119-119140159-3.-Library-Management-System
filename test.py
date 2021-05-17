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

def Show(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM subscribers")
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["subscriber_id","type","name","address","phone","email"], tablefmt="grid"))

def Insert(db):
    mycursor = db.cursor()
    print("\nInsert data subscriber")
    id_subs = input("Subscriber ID : ")
    tipe = input("Type : ")
    name = input("Name : ")
    address = input("Address : ")
    phone = input("Phone : ")
    email = input("Email : ")

    val = (id_subs, tipe, name, address, phone, email)
    sql = "INSERT INTO subscribers (subscriber_id, type, name, address, phone, email) VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data saved".format(mycursor.rowcount))

def Update(db):
    cursor = db.cursor()
    Show(db)
    id_subs = input("pilih id subscriber : ")
    tipe = input("Type : ")
    name = input("Name : ")
    address = input("Address : ")
    phone = input("Phone : ")
    email = input("Email : ")

    sql = "UPDATE subscribers SET type=%s, name=%s, address=%s, phone=%s, email=%s WHERE subscriber_id=%s"
    val = (tipe, name, address, phone, email, id_subs)
    cursor.execute(sql, val)
    db.commit()
    print("{} data changed".format(cursor.rowcount))

def Delete(db):
    cursor = db.cursor()
    Show(db)
    id_subs = input("pilih id subscriber :")
    sql = "DELETE FROM subscribers WHERE subscriber_id=%s"
    val = [id_subs]
    cursor.execute(sql,val)
    db.commit()
    print("{} data deleted".format(cursor.rowcount))
	
def Subscribers(db):
    while(True):
        print("\nSubscribers Menu")
        print('1. Show data')
        print('2. Insert data')
        print('3. Update data')
        print('4. Delete data')
        print('5. Quit')
        pilih = input("Choose Menu : ")
        if pilih == "1":
            Show(db)
        elif pilih == "2":
            Insert(db)
        elif pilih == "3":
            Update(db)
        elif pilih == "4":
            Delete(db)
        elif pilih == "5":
            pass
        else :
            print("You inputed the wrong menu, please try again")

def Denda(db,id_borrow,data_type):
    mycursor = db.cursor()
    val = [id_borrow]
    if data_type == "regular":
        sql = "SELECT DATEDIFF(return_date, borrow_date + INTERVAL '21' DAY) FROM borrowing WHERE borrowing_id = (%s)"
    elif data_type == "golden":
        sql = "SELECT DATEDIFF(return_date, borrow_date + INTERVAL '90' DAY) FROM borrowing WHERE borrowing_id = (%s)"
    
    mycursor.execute(sql,val)
    myresult3 = mycursor.fetchone()
    for i in myresult3:
        tenggat = i
        
    if tenggat > 0 :
        fee = tenggat*2000
        print("Returning Success, but you've got fee for",tenggat,"days, about",fee)
        valFee = (fee, id_borrow)
        sqlFee = "UPDATE borrowing SET fee = (%s) WHERE borrowing_id = (%s)"
        mycursor.execute(sqlFee,valFee)
        db.commit()
    else :
        print("Returning Success")
        fee = 0
        valFee = (fee, id_borrow)
        sqlFee = "UPDATE borrowing SET fee = (%s) WHERE borrowing_id = (%s)"
        mycursor.execute(sqlFee,valFee)
        db.commit()

    val1 = [id_borrow]
    sql1 = "SELECT * FROM borrowing WHERE borrowing_id = (%s)"
    mycursor.execute(sql1, val1)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["borrowing_id","subscriber_id","borrow_date","item_id","return_date","fee"], tablefmt="grid"))
	
def Borrowing(db):
    def hasil(a, db):
    	mycursor = db.cursor()
    	val1 = [a]
        sql1 = "SELECT item_id, library_id, title FROM items NATURAL JOIN borrowing WHERE borrowing_id = (%s)"
        mycursor.execute(sql1, val1)
        myresult = mycursor.fetchall()
        print("Anda meminjam: ")
        print(tabulate(myresult, headers=["item_id", "library_id", "title"], tablefmt="grid"))
	
    print("Insert data borrowing")
    id_borrow = int(input("Borrowing ID : "))
    id_subs = int(input("Subscriber ID : "))
    borrow_date = input("Borrowing date : ")
    item_id = input("Item id : ")
    
    mycursor = db.cursor()
    val = (id_borrow, id_subs, item_id, borrow_date)
    sql = "INSERT INTO borrowing (borrowing_id, subscriber_id, item_id, borrow_date) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql,val)
    db.commit()
    hasil(id_borrow, db)
    print("{} data saved".format(mycursor.rowcount))

def Returning(db):
    def hasil(db, a):
        mycursor = db.cursor()
        val = [a]
        sql = "SELECT DATEDIFF(return_date, borrow_date) FROM borrowing WHERE borrowing_id = (%s)"
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
	print(tabulate(myresult, headers=["overdue 'day(s)'"], tablefmt="grid"))
	
    id_borrow = int(input("Borrowing ID : "))
    return_date = input("Returning date : ")
    mycursor = db.cursor()
    val = (return_date, id_borrow)
    sql = "UPDATE borrowing SET return_date = (%s) WHERE borrowing_id = (%s)"
    mycursor.execute(sql, val)
    db.commit()
    hasil(db, id_borrow)
    print("{} item returned\n".format(mycursor.rowcount))
    
    # if val == 'regular' :
    #     tgl1 = borrow_date.dd()
    #     tgl1 + 
    
    # elif val == 'golden' :

def Menu(db):
    print('=== WELCOME TO LIBRARY MANAGEMENT SYSTEM ===')
    print("=== Library Menu ===")
    print("1. List of Library")
    print("2. Subscribers")
    print("3. Borrowing")
    print("4. Returning")
    print("5. Quit")
    pilih_menu = input("Choose Menu : ")

    if pilih_menu == "1":
    	Library(db)
    	Items(db)
    elif pilih_menu == "2":
    	Subscribers(db)
    elif pilih_menu == "3":
        Borrowing(db)
    elif pilih_menu == "4":
        Returning(db)
    elif pilih_menu == "5":
        exit()
    else:
        print("You inputed the wrong menu, please try again")

while(True):
	Menu(db)
