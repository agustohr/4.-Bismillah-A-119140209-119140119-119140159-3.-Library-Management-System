import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='root',
    password='',
    database='library_management_system'
)

mycursor = db.cursor()
mycursor.execute("SELECT * FROM library")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

a = input(int('insert library_id : '))

class Items :
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM items WHERE pilih ")
    myresult = mycursor.fetchall()
    
    db.commit()
    
# class Subscibers :
#     mycursor = db.cursor()
#     # a = input(int('insert subscriber_id : '))
#     # b = input('insert type : ')
#     # c = input('insert name : ')
#     # d = input('insert address : ')
#     sql = "INSERT INTO subscribers (subscriber_id, type, name, address, phone, email) VALUES (%s, %s, %s, %s, %s, %s)"
#     val = [
#       (1, 1, 'Lowstreet 4', 'a', 'b', 'c', 'd', 'e'),
#       (2, 2, 'Lowstreet 4', 'a', 'b', 'c', 'd', 'e'),
#       (3, 3, 'Lowstreet 4', 'a', 'b', 'c', 'd', 'e')
#     ]
#     mycursor.execute(sql, val)

#     db.commit()

# # print('Library menu')
# # print('1. Main Campus Library')
# # print('2. Computer Science Library')
# # print('3. Engineering Library')
# # a = input(int('Choose library menu : '))
