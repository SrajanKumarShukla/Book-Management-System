import tkinter as tk
from PIL import ImageTk,Image
import sqlite3 as sql
from tkinter import messagebox
root=tk.Tk()
root.title('Book Management System')
root.geometry('500x500+50+50')
username=tk.StringVar()
address=tk.StringVar()
gender=tk.StringVar()
mobile=tk.IntVar()
email=tk.StringVar()
password=tk.StringVar()
username_c=tk.StringVar()
password_c=tk.StringVar()
notice=tk.StringVar()
book_name=tk.StringVar()
root2=tk.StringVar()
root3=tk.StringVar()
root4=tk.StringVar()
root5=tk.StringVar()
root6=tk.StringVar()
root1=tk.StringVar()
#database

def database():
    global username
    global address
    global gender
    global email
    global mobile
    global password
    conn=sql.connect('userdetail.db')
    c=conn.cursor()
    l=[username.get(),address.get(),gender.get(),mobile.get(),email.get(),password.get()]
    c.execute("insert into userdetail values(?,?,?,?,?,?)",l)
    for row in c.execute('select * from userdetail'):
        print(row)
    conn.commit()
    conn.close()
    
def submit():
    global book_name
    global root3

    root3=tk.Tk()
    root3.title('Submit')
    root3.geometry('500x500+50+50')
    fieldset4=tk.Label(root3,relief='groove')
    fieldset4.place(x=50,y=46,height=400,width=400)
    f4label=tk.Label(root3,text='Submit Book',font=40,fg='white',bg='dodgerblue',padx=151.5)
    f4label.place(x=50,y=22,)
    l1=tk.Label(root3,text='Select Book :',font=30)
    l1.place(x=100,y=80)
    #
    book_name=tk.StringVar(root3)
    book_name.set('Select a book')
    b=tk.OptionMenu(root3,book_name,"Python","Algorithms","Architecture","C++","C","Data Structure","Graphics","DBMS","Softskill","Mechanics","Civil","How to C")
    b.place(x=210,y=75)
    
    b1=tk.Button(root3,text='Submit',fg='white',bg='dodgerblue',padx=30,command=status_submit)
    b1.place(x=220,y=123)
    root3.mainloop()
    root4.destroy()
def status_submit():
    
    conn=sql.connect('record.db')
    c=conn.cursor()
    c.execute('update book set status=(?) where name=(?)',("",book_name.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo(title='Submit',message="Book has been submitted!")
    root3.destroy()
def request():
    global book_name
    global root5
    root5=tk.Tk()
    root5.title('Request')
    root5.geometry('500x500+50+50')
    fieldset4=tk.Label(root5,relief='groove')
    fieldset4.place(x=50,y=46,height=400,width=400)
    f4label=tk.Label(root5,text='Submit Book',font=40,fg='white',bg='dodgerblue',padx=151.5)
    f4label.place(x=50,y=22)
    l1=tk.Label(root5,text='Select Book :',font=30)
    l1.place(x=100,y=80)
    #
    book_name=tk.StringVar(root5)
    book_name.set('Select a book')
    b=tk.OptionMenu(root5,book_name,"Python","Algorithms","Architecture","C++","C","Data Structure","Graphics","DBMS","Softskill","Mechanics","Civil","How to C")
    b.place(x=210,y=75)
    
    b1=tk.Button(root5,text='Request',fg='white',bg='dodgerblue',padx=30,command=status_request)
    b1.place(x=220,y=123)
    root5.mainloop()
    root4.destroy()
def status_request():
    conn=sql.connect('record.db')
    c=conn.cursor()
    print(username_c.get(),book_name.get())
    c.execute('update book set status=(?) where name=(?)',(username_c.get(),book_name.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo(title='Request',message="Book has been issued!")
    root5.destroy()
def sub_req():
    global username_c
    global password_c
    global root5
    conn=sql.connect('userdetail.db')
    c=conn.cursor()
    for row in c.execute('select name,password from userdetail'):
        if(row==(username_c.get(),password_c.get(),)):
            root4=tk.Tk()
            root4.title('SUBMIT AND REQUEST BOOK')
            root4.geometry('500x500+50+50')
            l1=tk.Label(root4,relief='groove')
            l1.place(x=50,y=46,height=400,width=400)
            l2=tk.Label(root4,text='SUBMIT AND REQUEST BOOK',font=40,fg='white',bg='dodgerblue',padx=85)
            l2.place(x=50,y=22)
            l3=tk.Button(root4,text='Submit Book',font=30,fg='white',bg='dodgerblue',padx=20,command=submit)
            l3.place(x=190,y=100)
            l4=tk.Button(root4,text='Request Book',font=30,fg='white',bg='dodgerblue',padx=15,command=request)
            l4.place(x=190,y=150)
            root4.mainloop()
            break
        root1.destroy()
##login
def login():
    root.destroy()
    global username_c
    global password_c
    global root1
    root1=tk.Tk()
    root1.title('Login')
    root1.geometry('500x500+50+50')
    fieldset2=tk.Label(root1,relief='groove')
    fieldset2.place(x=50,y=46,height=400,width=400)
    f2label=tk.Label(root1,text='Login',fg='white',bg='dodgerblue',font=40,padx=178)
    f2label.place(x=50,y=22)
    #username
    l2=tk.Label(root1,text='Username :',font=30)
    l2.place(x=100,y=100)
    username_c=tk.Entry(root1,width=30)
    username_c.place(x=200,y=103)
    passw=tk.Label(root1,text='Password :',font=30)
    passw.place(x=100,y=140)
    password_c=tk.Entry(root1,show='*',width=30)
    password_c.place(x=200,y=143)
    b4=tk.Button(root1,text='Login',bg='dodgerblue',fg='white',padx=30,command=sub_req)
    b4.place(x=230,y=180)
    l6=tk.Label(root1,text='Or',fg='green')
    l6.place(x=270,y=210)
    b6=tk.Button(root1,text='SignUp',fg='white',bg='dodgerblue',padx=26,command=register)
    b6.place(x=230,y=232)
    root1.mainloop()
    img=ImageTk.PhotoImage(root1,Image.open('b3.png'))
    imglabel=tk.Label(root1,image=img,width=391,height=192)
    imglabel.image=img
    imglabel.place(x=52,y=245)
##register
def available():
    root1.destroy()
    global root6
    root6=tk.Tk()
    root6.title('Available Books')
    root6.geometry('500x500+50+50')
    fieldset4=tk.Label(root6,relief='groove')
    fieldset4.place(x=50,y=7,height=400,width=400)
    tk.Label(root6,text='Book Name').place(x=150,y=10)
    tk.Label(root6,text='Price').place(x=320,y=10)
    tk.Label(root6,text='------------------------------------------').place(x=150,y=30)
    tk.Label(root6,text='Python').place(x=150,y=50)
    tk.Label(root6,text='400').place(x=320,y=50)
    tk.Label(root6,text='Algorithms').place(x=150,y=70)
    tk.Label(root6,text='450').place(x=320,y=70)
    tk.Label(root6,text='Architecture').place(x=150,y=90)
    tk.Label(root6,text='500').place(x=320,y=90)
    tk.Label(root6,text='C++').place(x=150,y=110)
    tk.Label(root6,text='200').place(x=320,y=110)
    tk.Label(root6,text='C').place(x=150,y=130)
    tk.Label(root6,text='300').place(x=320,y=130)
    tk.Label(root6,text='Data Structure').place(x=150,y=130)
    tk.Label(root6,text='350').place(x=320,y=130)
    tk.Label(root6,text='Graphics').place(x=150,y=150)
    tk.Label(root6,text='450').place(x=320,y=150)
    tk.Label(root6,text='DBMS').place(x=150,y=170)
    tk.Label(root6,text='550').place(x=320,y=170)
    tk.Label(root6,text='Softskill').place(x=150,y=190)
    tk.Label(root6,text='150').place(x=320,y=190)
    tk.Label(root6,text='Mechanics').place(x=150,y=210)
    tk.Label(root6,text='300').place(x=320,y=210)
    tk.Label(root6,text='Civil').place(x=150,y=230)
    tk.Label(root6,text='600').place(x=320,y=230)
    tk.Label(root6,text='How to C').place(x=150,y=250)
    tk.Label(root6,text='350').place(x=320,y=250)
    
   

    
    root6.mainloop()
def register():
    global username
    global address
    global gender
    global email
    global mobile
    global password
    global root2
    root2=tk.Tk()
    root2.title('Register')
    root2.geometry('500x500+50+50')
    fieldset3=tk.Label(root2,relief='groove')
    fieldset3.place(x=50,y=46,height=400,width=400)
    f3label=tk.Label(root2,text='Register',fg='white',bg='dodgerblue',font=40,padx=168)
    f3label.place(x=50,y=22)
    l6=tk.Label(root2,text='Username :',font=30)
    l6.place(x=100,y=80)
    username=tk.Entry(root2,width=30)
    username.place(x=200,y=83)
    l8=tk.Label(root2,text='Address :',font=30)
    l8.place(x=100,y=120)
    address=tk.Entry(root2,width=30)
    address.place(x=200,y=123)
    l10=tk.Label(root2,text='Gender :',font=30)
    l10.place(x=100,y=160)
    gender=tk.Entry(root2,width=5)
    gender.place(x=200,y=160)
    g=tk.Label(root2,text='M or F',fg='green')
    g.place(x=230,y=160)
    l11=tk.Label(root2,text='Mobile :',font=30)
    l11.place(x=100,y=200)
    mobile=tk.Entry(root2,width=30)
    mobile.place(x=200,y=203)
    l13=tk.Label(root2,text='Email :',font=30)
    l13.place(x=100,y=240)
    email=tk.Entry(root2,width=30)
    email.place(x=200,y=243)
    l15=tk.Label(root2,text='Password',font=30)
    l15.place(x=100,y=280)
    password=tk.Entry(root2,show='*',width=30)
    password.place(x=200,y=283)
    b5=tk.Button(root2,text='Register',fg='white',bg='dodgerblue',font=('',10),padx=20,command=database)
    b5.place(x=200,y=320)
    root2.mainloop()
    root2.destroy()
    root1.destroy()

##front page
fieldset_1=tk.Label(root,relief='groove')
fieldset_1.place(x=50,y=46,height=400,width=400)
flabel=tk.Label(root,text='Book Management System',bg='dodgerblue',fg='white',font=40,padx=104)
flabel.place(x=50,y=22)
b1=tk.Button(root,text='Login',fg='white',bg='dodgerblue',padx=30,command=login)
b1.place(x=70,y=200)
b2=tk.Button(root,text='Sign Up',fg='white',bg='dodgerblue',padx=25,command=register)
b2.place(x=186,y=200)
b3=tk.Button(root,text='Available Books',fg='white',bg='dodgerblue',padx=10,command=available)
b3.place(x=300,y=200)
l1=tk.Label(root,text='\"All the knowledge you can bank on \nand applying that knowledge \nto produce outstanding work\"',font=('Rockwell',17),fg='green')
l1.place(x=52,y=70)
img=ImageTk.PhotoImage(Image.open('b3.png'))
imglabel=tk.Label(image=img,width=391,height=192)
imglabel.image=img
imglabel.place(x=52,y=245)
root.mainloop()
