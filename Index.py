from tkinter import *
from tkinter import messagebox,ttk
import DataBaser

#Janela

jan = Tk()
jan.title("IA Soluctions - Access Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.91)
jan.iconbitmap(default="Icons/LogoIcon.ico")

#IMGs
logo = PhotoImage(file="Icons/logo.png")

#WIDGETS
RightFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LeftFrame = Frame(jan, width=399, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

LogoLabel = Label(RightFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

#Campos

UserLabel = Label(LeftFrame, text="Username: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(LeftFrame, width=30)
UserEntry.place(x=150, y=111)

PassLabel = Label(LeftFrame, text="Password: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(LeftFrame, width=30, show="*")
PassEntry.place(x=150, y=161)

#Botoes

def Login():
    UserLogin = UserEntry.get()
    PasswordLogin = PassEntry.get()
    DataBaser.cur.execute("""
    SELECT * FROM Users
    WHERE (User = ? AND Password = ?)
    """, (UserLogin, PasswordLogin))
    Verify = DataBaser.cur.fetchone()
    try:   
        if (UserLogin in Verify and PasswordLogin in Verify):
            messagebox.showinfo(title="Access Info", message="Login Sucessfull, Welcome!")
    except:
        messagebox.showerror(title="Access Info", message="Login Failed, Not Registered")


LoginButton = ttk.Button(LeftFrame, text="Login", width="30", command=Login)
LoginButton.place(x=100, y=225)

def Register():

    LoginButton.place(x=9000)
    RegisterButton.place(x=10000)

    NomeLabel = Label(LeftFrame, text="Name: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(LeftFrame, width=39)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(LeftFrame, text="Email: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(LeftFrame, width=39)
    EmailEntry.place(x=100, y=66)

    def RegistertoDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Password = PassEntry.get()
        
        if (Name == "" or Email == "" or User == "" or Password == ""):
            messagebox.showerror(title="Register Error", message="Não deixe nenhum vazio")
        else:
            DataBaser.cur.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Password))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Account Created With Sucess")


    Register = ttk.Button(LeftFrame, text="Register", width="30", command=RegistertoDataBase)
    Register.place(x=100, y=225)

    def Back():
        NomeLabel.place(x=9000)
        NomeEntry.place(x=10000)
        EmailEntry.place(x=11000)
        EmailLabel.place(x=12000)
        Register.place(x=13000)
        Back.place(x=14000)
        RegisterButton.place(x=130)
        LoginButton.place(x=100)

    Back = ttk.Button(LeftFrame, text="Back", width="20", command=Back)
    Back.place(x=130, y=260)




RegisterButton = ttk.Button(LeftFrame, text="Register", width="20", command=Register)
RegisterButton.place(x=130, y=260)



#Acaba a instrução da janela com mainloop
jan.mainloop()



