import sqlite3
import tkinter as tk
from tkinter import ttk 

con=sqlite3.connect("students.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS student (id INT, name TEXT, grade INT)")
con.commit()

def writeDatabase():
  try:
    _id=int(id.get())
    _name=str(name.get())
    _grade=int(grade.get())
    is_succes=True
    cursor.execute("SELECT id FROM student")
    data= list(cursor.fetchall())
    print(data)
    for j in data:
      for k in j:
        print(type(k))
        if _id==k:
          is_succes=False
      
    for i in _name:
      if i =="1" or i =="2" or i =="3" or i =="4" or i =="5" or i =="6" or i =="7" or i =="8" or i =="9" or i =="0":
        print("girdi")
        is_succes=False

    if _grade >= 0 and _grade <= 100 and is_succes:
      cursor.execute("INSERT INTO student (id,name,grade) VALUES (?,?,?)",(_id,_name,_grade))
      con.commit()
      id.delete(0,tk.END)
      name.delete(0,tk.END)
      grade.delete(0,tk.END)
      print(_id,_name,_grade)
      print("success")
      label_state.config(text="succes",foreground="green")
    else:
      label_state.config(text="fail",foreground="red")
  except ValueError:
    label_state.config(text="fail",foreground="red")


def readDatabase():
  _id=ara.get()
  cursor.execute(f"SELECT * FROM student WHERE id = {_id}")
  data=cursor.fetchall()
  if data==[]:
    print("ds")
    label_show_grade.config(text="There isn't student who has this id", foreground="red")
  else: 
    s:str=""
    for i in data:
      for k in i:
        s=s+" "+str(k)
    label_show_grade.config(text=s, foreground="black")


window=tk.Tk()
window.title('StudentDatabase')
window.geometry("400x400")
icon=tk.PhotoImage(file='graduated.png')
window.iconphoto(False,icon)


id = ttk.Entry(master=window)
name = ttk.Entry(master=window)
grade = ttk.Entry(master=window)
ara=ttk.Entry(master=window)
label_id=ttk.Label(text="Id")
label_name=ttk.Label(text="Name")
label_grade=ttk.Label(text="Grade")
label_state=ttk.Label(text="")
label_show_grade=ttk.Label(text="")
button= ttk.Button(master=window, text='Ekle', command=writeDatabase)
button2=ttk.Button(master=window, text='Ara', command=readDatabase)
ara.insert(0,"Student's Id")


label_id.place(x=10,y=10)
label_name.place(x=10,y=35)
label_grade.place(x=10,y=65)
label_state.place(x=240,y=30)
id.place(x=60,y=10)
name.place(x=60,y=35)
grade.place(x=60,y=65)
button.place(x=215,y=5)
button2.place(x=200,y=200)
ara.place(x=10,y=200)
label_show_grade.place(x=10,y=230)


window.mainloop()
con.close()
