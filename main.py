from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from db import Database



db=Database("Employee.db")
root=Tk()
root.title("Employee management system")        #title of main window
root.geometry("1920x1080+0+0")                  #geometry of main window
root.config(bg="#2c3e50")                       #background colour of main window
root.state("zoomed")                            #fit window to screen

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()
address = StringVar()

# Entries Frames
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Employee Management System", font=("calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2,padx=10,pady=20,sticky="w")

lblName=Label(entries_frame,text="NAME", font=("calibri",18), bg="#535c68", fg="white")
lblName.grid(row=1, column=0,padx=10,pady=5, sticky="w")
txtName=Entry(entries_frame,textvariable=name, font=("calibri",16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=5, sticky="w")

lblAge=Label(entries_frame,text="AGE", font=("calibri",18), bg="#535c68", fg="white")
lblAge.grid(row=1, column=2,padx=10,pady=5, sticky="w")
txtAge=Entry(entries_frame,textvariable=age, font=("calibri",16),width=30)
txtAge.grid(row=1,column=3,padx=10,pady=5, sticky="w")

lbldoj=Label(entries_frame,text="D.O.J", font=("calibri",18), bg="#535c68", fg="white")
lbldoj.grid(row=2, column=0,padx=10,pady=5, sticky="w")
txtdoj=Entry(entries_frame,textvariable=doj, font=("calibri",16),width=30)
txtdoj.grid(row=2,column=1,padx=10,pady=5, sticky="w")

lblEmail=Label(entries_frame,text="EMAIL", font=("calibri",18), bg="#535c68", fg="white")
lblEmail.grid(row=2, column=2,padx=10,pady=5, sticky="w")
txtEmail=Entry(entries_frame,textvariable=email, font=("calibri",16),width=30)
txtEmail.grid(row=2,column=3,padx=10,pady=5, sticky="w")

lblGender=Label(entries_frame,text="GENDER", font=("calibri",18), bg="#535c68", fg="white")
lblGender.grid(row=3, column=0,padx=10,pady=5, sticky="w")
txtGender=Entry(entries_frame,textvariable=gender, font=("calibri",16),width=30)
txtGender.grid(row=3,column=1,padx=10,pady=5, sticky="w")
comboGender=ttk.Combobox(entries_frame, font=("calibri",16),width=28,textvariable=gender)
comboGender['values']=("Male","Female","Other")
comboGender.grid(row=3,column=1,padx=10,pady=5,sticky="w")

lblContact=Label(entries_frame,text="CONTACT NO.", font=("calibri",18), bg="#535c68", fg="white")
lblContact.grid(row=3, column=2,padx=10,pady=5, sticky="w")
txtContact=Entry(entries_frame,textvariable=contact, font=("calibri",16),width=30)
txtContact.grid(row=3,column=3,padx=10,pady=5, sticky="w")

lblAddress=Label(entries_frame,text="ADDRESS", font=("calibri",18), bg="#535c68", fg="white")
lblAddress.grid(row=4, column=0,padx=10,pady=10, sticky="w")
txtAddress=Text(entries_frame,width=88,height=5,font=("calibri",16))
txtAddress.grid(row=5,column=0,columnspan=4,padx=10,pady=5, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END , row[7])


def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def add_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtdoj.get()=="" or txtEmail.get()=="" or comboGender.get()=="" or txtContact.get()=="" or txtAddress.get(1.0,END)=="":
        tkinter.messagebox.showerror("Error in Input","PLEASE FILL ALL THE DETAILS")
        return
    db.insert(txtName.get(),txtAge.get(),txtdoj.get(),txtEmail.get(),comboGender.get(),txtContact.get(),txtAddress.get(1.0,END))
    tkinter.messagebox.showinfo("SUCCESS","RECORD INSERTED")
    ClearAll()
    displayAll()

def update_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtdoj.get()=="" or txtEmail.get()=="" or comboGender.get()=="" or txtContact.get()=="" or txtAddress.get(1.0,END)=="":
        tkinter.messagebox.showerror("Error in Input","PLEASE FILL ALL THE DETAILS")
        return
    db.update(row[0],txtName.get(),txtAge.get(),txtdoj.get(),txtEmail.get(),comboGender.get(),txtContact.get(),txtAddress.get(1.0,END))
    tkinter.messagebox.showinfo("SUCCESS","RECORD UPDATED")
    ClearAll()
    displayAll()


def delete_employee():
    db.remove(row[0])
    tkinter.messagebox.showinfo("SUCCESS", "RECORD DELETED")
    ClearAll()
    displayAll()

def ClearAll():
    name.set("")
    age.set("")
    doj.set("")
    email.set("")
    gender.set("")
    contact.set("")
    txtAddress.delete(1.0,END)


def logout():
    root.destroy()
    import login


btn_frame=Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")

btnAdd=Button(btn_frame,command=add_employee,text="Add Details",width=15,font=("calibri",16,"bold"),fg="white",bg="#16a085",bd=0).grid(row=0,column=0,padx=10)
btnAdd=Button(btn_frame,command=update_employee,text="Update Details",width=15,font=("calibri",16,"bold"),fg="white",bg="#2980b9",bd=0).grid(row=0,column=1,padx=10)
btnAdd=Button(btn_frame,command=delete_employee,text="Delete Details",width=15,font=("calibri",16,"bold"),fg="white",bg="#c0392b",bd=0).grid(row=0,column=2,padx=10)
btnAdd=Button(btn_frame,command=ClearAll,text="Clear All",width=15,font=("calibri",16,"bold"),fg="white",bg="#f39c12",bd=0).grid(row=0,column=3,padx=10)
btnAdd=Button(btn_frame,command=logout,text="Logout",width=15,font=("calibri",16,"bold"),fg="white",bg="black",bd=0).grid(row=0,column=4,padx=10)

# Table Frames
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0,y=472,width=1550,height=520)
style=ttk.Style()
style.configure("mystyle.Treeview", font=("calibri",18),rowheight=50) #Modify the font of the body
style.configure("mystyle.Treeview.Heading",font=("calibri",18)) #Modify the heading of the table
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=2)
tv.heading("2",text="Name")
tv.column("2",width=15)
tv.heading("3",text="Age")
tv.column("3",width=3)
tv.heading("4",text="D.O.J")
tv.column("4",width=5)
tv.heading("5",text="Email")
tv.column("5",width=15)
tv.heading("6",text="Gender")
tv.column("6",width=5)
tv.heading("7",text="Contact")
tv.column("7",width=10)
tv.heading("8",text="Address")
tv['show']='headings'
tv.pack(fill=X)
tv.bind("<ButtonRelease-1>",getData)

displayAll()
root.mainloop()


