import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import mysql.connector
import os
root = tk.Tk()
root.title("Library Management System")
tabcontrol = ttk.Notebook(root)
library = ttk.Frame(tabcontrol)
labelFrame = ttk.LabelFrame(library,text="List of Library")
labelFrame.grid(column=0,row=0,padx=8,pady=4,sticky="N")

#*************************************************************

tabcontrol1 = ttk.Notebook(root)
Inventory1 = ttk.Frame(tabcontrol1)

labelFrame1 = ttk.LabelFrame(library,text="List of Library",borderwidth=3)

labelFrame1.grid(row=0,column=1,padx=8,pady=4,sticky="N")

Inventory1.pack()

#******************************** Fungsi Panel Daftar Pegawai *******************************
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="library_management_system"
)
i=0
def Get_data():
	global i
	global j
	i=0
	tree.delete(*tree.get_children())
	cursor = db.cursor()
	sql = "SELECT * FROM library"
	cursor.execute(sql)
	results = cursor.fetchall()
    
	for row in results:
		tree.insert('', 'end', text=str(i+1), values=(row[0],row[1]))
		i=i+1

#************************************ TREE VIEW *******************************************

tree = ttk.Treeview(labelFrame1, columns=('Library_id', 'Library_name'),height=20, show='headings')
tree.place(x=30, y=95)
vsb = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
vsb.place(x=30+954+5, y=0, height=200+220)

tree.configure(yscrollcommand=vsb.set)
tree.heading('#1', text='Library_id')
tree.heading('#2', text='Library_name')
tree.column('#1', stretch=tk.YES)
tree.column('#2', stretch=tk.YES)
tree.grid(row=11, columnspan=4, sticky='nsew')
tabcontrol1.pack(expand=0,fill="both")

ShowButton = ttk.Button(labelFrame,text='Show',command=Get_data, width=20)

style = ttk.Style()
style.configure('TButton', background='#3498db')

ShowButton.grid(column=0,row=9,sticky='W',pady=7)
tabcontrol.add(library,text='List of Library')
tabcontrol.pack(expand=1,fill="both")

root.mainloop()
