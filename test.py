import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='root',
    password='',
    database='library_system'
)
class Library :
    mycursor = db.cursor()
    sql = "INSERT INTO library (library_id, library_name) VALUES (%s, %s)"
    val = (2, "Book")
    mycursor.execute(sql, val)

    db.commit()

# class Items(Library) :
#     mycursor = db.cursor()
#     sql = "INSERT INTO items (item_id, library_id, category, title) VALUES (%s, %s)"
#     val = (2, "Book")
#     mycursor.execute(sql, val)

#     db.commit()
    
# print('Library menu')
# print('1. Main Campus Library')
# print('2. Computer Science Library')
# print('3. Engineering Library')
# pilih = input(int('Choose library menu : '))