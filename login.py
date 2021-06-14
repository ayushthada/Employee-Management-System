from tkinter import*
from PIL import ImageTk
from tkinter import messagebox




class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("850x600+100+50")#1199x600
        self.root.resizable(False,False)
        #background image
        self.bg=ImageTk.PhotoImage(file="login.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #login frame
        Frame_login=Frame(self.root,bg="gray")
        Frame_login.place(x=150,y=150,height=340,width=500)


        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="black",bg="gray").place(x=90,y=30)
        desc=Label(Frame_login,text="Company Login Area",font=("Goudy old style",15,"bold"),fg="black",bg="gray").place(x=90,y=100)

        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="black",bg="gray").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("Calibri",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="black",bg="gray").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("Calibri",15),show="*",bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        #forget_btn =Button(Frame_login,text="Forgot Password?",cursor="hand2",bg="gray",fg="black",bd=0,font=("Goudy old style",12)).place(x=90,y=280)
        Login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Login",fg="gray",bg="black",font=("Goudy old style",20)).place(x=300,y=470,width=180,height=40)

    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_user.get()!="admin" or self.txt_pass.get()!="ems1234":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            self.root.destroy()
            import main


root=Tk()
obj=Login(root)
root.mainloop()
