#Bismillah-A-Library-Management-System
#TUBES PBO
import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='root',
    password='',
    database='library_management_system'
)
# library_id = input(int('masukkan id = '))
# library_name = input(str('masukkan nama = '))
# library_id = 2
# library_name = 'book'
mycursor = db.cursor()
sql = "INSERT INTO library (library_id, library_name) VALUES (%s, %s)"
val = (2, "Book")
mycursor.execute(sql, val)

db.commit()
