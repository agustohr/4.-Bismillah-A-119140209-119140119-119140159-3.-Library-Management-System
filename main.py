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
	
class SubsCRUD(ConnectSql):
    def __init__(self,id_subs,tipe,name,address,phone,email):
        self.__id_subs      = id_subs
        self.__tipe         = tipe
        self.__name         = name
        self.__address      = address
        self.__phone        = phone
        self.__email        = email        
        super().__init__()
        super().createConnection
        self.__db = self.createConnection

    def create(self):
        cursor = self.__db.cursor()
        val = (self.__id_subs, self.__tipe, self.__name, self.__address, self.__phone, self.__email)
        cursor.execute("INSERT INTO subscribers (subscriber_id, type, name, address, phone, email) VALUES (%s,%s,%s,%s,%s,%s)", val)
        self.__db.commit()

        print(cursor.rowcount, "record inserted.")

    def read(self):
        cursor = self.__db.cursor()
        cursor.execute("SELECT * FROM subscribers")
        myresult = cursor.fetchall()

        print(tabulate(myresult, headers=["subscriber_id","type","name","address","phone","email"], tablefmt="grid"))

    def update(self):
        cursor = self.__db.cursor()
        val = (self.__tipe, self.__name, self.__address, self.__phone, self.__email, self.__id_subs)
        cursor.execute ("UPDATE subscribers SET type=%s, name=%s, address=%s, phone=%s, email=%s WHERE subscriber_id=%s ", val)
        self.__db.commit()

        print(cursor.rowcount, "record updated.")

    def delete(self):
        cursor = self.__db.cursor()
        cursor.execute ("DELETE FROM subscribers WHERE subscriber_id = %s", (self.__id_subs,))
        self.__db.commit()

        print(cursor.rowcount, "record deleted.")

def SubsMenu():
    while(True):
        print("\nSubscribers Menu")
        print('1. Show data')
        print('2. Insert data')
        print('3. Update data')
        print('4. Delete data')
        print('5. Quit')
        pilih = input("Choose Menu (1-5): ")
        if pilih == "1":
            subs = SubsCRUD(0,0,0,0,0,0)
            subs.read()
        elif pilih == "2":
            subs = SubsCRUD(0,0,0,0,0,0)
            subs.read()
            print("Insert Subscriber Data")
            id_subs = input("Subscriber ID : ")
            print("\ngolden : golden subscribers can borrow for three months")
            print("regular : regular subscribers can borrow for three weeks")
            
            while(True):
                tipe = input("Type (regular/golden): ")
                if (tipe == "regular") or (tipe == "golden"):
                    break
                else:
                    print("You input the wrong type, please try again")
            name = input("Name : ")
            address = input("Address : ")
            phone = input("Phone : ")
            email = input("Email : ")
            subs = SubsCRUD(id_subs,tipe,name,address,phone,email)
            subs.create()
            
        elif pilih == "3":
            subs = SubsCRUD(0,0,0,0,0,0)
            subs.read()
            print("Update Subscriber Data")
            id_subs = input("Search by ID subscriber : ")
            print("Edit")
            tipe = input("Type (regular/golden): ")
            name = input("Name : ")
            address = input("Address : ")
            phone = input("Phone : ")
            email = input("Email : ")
            subs = SubsCRUD(id_subs,tipe,name,address,phone,email)
            subs.update()
        elif pilih == "4":
            subs = SubsCRUD(0,0,0,0,0,0)
            subs.read()
            print("Delete Subscriber Data")
            id_subs = input('Search by subscriber ID to delete :')
            subs = SubsCRUD(id_subs,0,0,0,0,0)
            subs.delete()
        elif pilih == "5":
            os.system("cls")
            break
        else :
            print("You input the wrong menu, please try again")

def SubsMenuAdmin():
    while(True):
        print("\nSubscribers Menu")
        print('1. Show data')
        print('2. Delete data')
        print('3. Quit')
        pilih = input("Choose Menu (1-3): ")
        if pilih == "1":
            subs = SubsCRUD(0,0,0,0,0,0)
            subs.read()
        elif pilih == "2":
            subs = SubsCRUD(0,0,0,0,0,0)
            subs.read()
            print("Delete Subscriber Data")
            id_subs = input('Search by subscriber ID to delete :')
            subs = SubsCRUD(id_subs,0,0,0,0,0)
            subs.delete()
        elif pilih == "3":
            os.system("cls")
            break
        else :
            print("You input the wrong menu, please try again")
