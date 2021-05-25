import mysql.connector as mysql
import os
from tabulate import tabulate

class ConnectSql:
    def __init__(self):
        self.__localhost     = "localhost"
        self.__username      = "root"
        self.__password      = ""
        self.__database_name = "library_management_system"
        self.createConnection
    
    @property
    def createConnection(self):
        db = mysql.connect(
          host     = self.__localhost,
          user     = self.__username,
          passwd   = self.__password,
          database = self.__database_name
        )
        return db

class showItems(ConnectSql):
    def __init__(self,idLbr,item_id,library_id,category,title,author,publisher,production_year,copies):
        self.__idLbr            = idLbr
        self.__item_id          = item_id 
        self.__library_id       = library_id
        self.__category         = category
        self.__title            = title
        self.__author           = author
        self.__publisher        = publisher
        self.__production_year  = production_year
        self.__copies           = copies
        super().__init__()
        super().createConnection
        self.__db = self.createConnection

    def Library(self):
        mycursor = self.__db.cursor()
        mycursor.execute("SELECT * FROM library")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=["library_id","library_name"], tablefmt="grid"))

    def ItemsById(self):
        mycursor = self.__db.cursor()
        sql = "SELECT * FROM items WHERE library_id=%s"
        val = [self.__idLbr]
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=["item_id","library_id","category","title","author","publisher","production_year","copies"], tablefmt="grid"))

    def ReadItems(self):
        mycursor = self.__db.cursor()
        mycursor.execute("SELECT * FROM items")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=["item_id","library_id","category","title","author","publisher","production_year","copies"], tablefmt="grid"))

    def CreateItems(self):
        mycursor = self.__db.cursor()
        val = (self.__item_id, self.__library_id, self.__category, self.__title, self.__author, self.__publisher, self.__production_year, self.__copies)
        mycursor.execute("INSERT INTO items (item_id, library_id, category, title, author, publisher, production_year, copies) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", val)
        self.__db.commit()

        print(mycursor.rowcount, "record inserted.")

    def UpdateItems(self):
        mycursor = self.__db.cursor()
        val = (self.__library_id,self.__category,self.__title,self.__author,self.__publisher,self.__production_year,self.__copies,self.__item_id)
        mycursor.execute ("UPDATE items SET library_id=%s, category=%s, title=%s, author=%s, publisher=%s, production_year=%s, copies=%s WHERE item_id=%s ", val)
        self.__db.commit()

        print(mycursor.rowcount, "record updated.")

    def DeleteItems(self):
        mycursor = self.__db.cursor()
        mycursor.execute ("DELETE FROM items WHERE item_id = %s", (self.__item_id,))
        self.__db.commit()

        print(mycursor.rowcount, "record deleted.")
	
def ItemsMenu():
    while(True):
        print("\nItems Menu")
        print('1. Show data')
        print('2. Insert data')
        print('3. Update data')
        print('4. Delete data')
        print('5. Quit')
        pilih = input("Choose Menu (1-5): ")

        if pilih == "1":
            item = showItems(0,0,0,0,0,0,0,0,0)
            item.ReadItems()

        elif pilih == "2":
            item = showItems(0,0,0,0,0,0,0,0,0)
            item.ReadItems()
            print("Insert Items Data")
            item_id = input("Item ID : ")
            library_id = input("Library ID : ")
            category = input("Category : ")
            title = input("Title : ")
            author = input("Author : ")
            publisher = input("Publisher : ")
            production_year = input("Production year : ")
            copies = input("Copies : ")
            itemC = showItems(0,item_id,library_id,category,title,author,publisher,production_year,copies)
            itemC.CreateItems()
            
        elif pilih == "3":
            item = showItems(0,0,0,0,0,0,0,0,0)
            item.ReadItems()
            print("Update Items Data")
            item_id = input("Search by item ID : ")
            print("Edit")
            library_id = input("Library ID : ")
            category = input("Category : ")
            title = input("Title : ")
            author = input("Author : ")
            publisher = input("Publisher : ")
            production_year = input("Production year : ")
            copies = input("Copies : ")
            itemU = showItems(0,item_id,library_id,category,title,author,publisher,production_year,copies)
            itemU.UpdateItems()

        elif pilih == "4":
            item = showItems(0,0,0,0,0,0,0,0,0)
            item.ReadItems()
            print("Delete Items Data")
            item_id = input('Search by item ID to delete :')
            itemD = showItems(0,item_id,0,0,0,0,0,0,0)
            itemD.DeleteItems()

        elif pilih == "5":
            os.system("cls")
            break
        else :
            print("You input the wrong menu, please try again")
	
def Subscribers(db):
    while(True):
        print("\nSubscribers Menu")
        print('1. Show Data')
        print('2. Insert Data')
        print('3. Update Data')
        print('4. Delete Data')
        print('5. Back to Main Menu')
        pilih = input("Choose Menu [1-5] : ")
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
            print("You input the wrong menu, please try again")

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
        print("Returning Success, but you've been late for",tenggat,"day(s), and got penalty about",fee)
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
    Show(db)
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM borrowing")
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["borrowing_id","subscriber_id","borrow_date","item_id","return_date","fee"], tablefmt="grid"))

    print("\nInsert data of the borrowing item")
    id_borrow = int(input("Borrowing ID : "))
    id_subs = int(input("Subscriber ID : "))
    borrow_date = input("Borrowing date : ")
    item_id = input("Item id : ")
    
    val = (id_borrow, id_subs, item_id, borrow_date)
    sql = "INSERT INTO borrowing (borrowing_id, subscriber_id, item_id, borrow_date) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data saved".format(mycursor.rowcount))

    valIdb = [item_id]
    sqlCop = "UPDATE items SET copies = copies - 1 WHERE item_id = (%s)"
    mycursor.execute(sqlCop,valIdb)
    db.commit()

    val1 = [id_borrow]
    sql1 = "SELECT * FROM borrowing WHERE borrowing_id = (%s)"
    mycursor.execute(sql1, val1)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["borrowing_id","subscriber_id","borrow_date","item_id","return_date","fee"], tablefmt="grid"))

def Returning(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM borrowing")
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["borrowing_id","subscriber_id","borrow_date","item_id","return_date","fee"], tablefmt="grid"))

    print("Insert data of the returning item")
    id_subs = int(input("Subscriber ID : ")) 
    id_borrow = int(input("Borrowing ID : "))
    return_date = input("Returning date : ")
    val = (return_date, id_borrow)
    sql = "UPDATE borrowing SET return_date = (%s) WHERE borrowing_id = (%s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data saved".format(mycursor.rowcount))

    valIdt = [id_borrow]
    sqlIdt = "SELECT item_id FROM borrowing WHERE borrowing_id = %s"
    mycursor.execute(sqlIdt,valIdt)
    resultId = mycursor.fetchone()
    for i in resultId:
        item_id = i

    valIdb = [item_id]
    sqlCop = "UPDATE items SET copies = copies + 1 WHERE item_id = (%s)"
    mycursor.execute(sqlCop,valIdb)
    db.commit()
    
    valsub = [id_subs]
    sqlsub = "SELECT type FROM subscribers WHERE subscriber_id = %s"
    mycursor.execute(sqlsub,valsub)
    myresultsub = mycursor.fetchone()
    data_type = []
    for i in myresultsub:
        data_type.append(i)
    data_type = ''.join(data_type)

    Denda(db,id_borrow,data_type)

def Menu(db):
    print('=== WELCOME TO LIBRARY MANAGEMENT SYSTEM ===')
    print("\n=== Library Menu ===")
    print("1. List of Library and Items")
    print("2. Subscribers")
    print("3. Borrow Item")
    print("4. Return Item")
    print("5. Exit")
    print("\nChoose [1] Before If You Want to Borrow The Item")
    pilih_menu = input("Choose Menu [1-5] : ")

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
        print("You input the wrong menu, please try again")

while(True):
	Menu(db)
