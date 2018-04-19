
                            #Import module
from Tkinter import *
import Tkinter
import sqlite3
import tkMessageBox
from sqlite3 import OperationalError


                            #Student's  Login
global username
def login():
    newUser=Toplevel(main)
    newUser.title("Login Page")
    UserName = Label(newUser,text="User Name",width=45)
    UserName.pack()
    UserNameVal= Entry(newUser,width=45)
    UserNameVal.pack()
    Password = Label(newUser,text="Password",width=45)
    Password.pack()
    Passwordval=Entry(newUser,show="*",width=45)
    Passwordval.pack()
    def login_now():
        global username,supera
        name=UserNameVal.get()
        password= Passwordval.get()
        if(name=='' or password==''):
            tkMessageBox.showinfo("Missing Value","Username or password empty!")
            return
        else:
            conn = sqlite3.connect('student.db')
            try:
                content=conn.execute("SELECT NAME,PASSWORD,SUPERVISOR FROM STUDENTS");
            except OperationalError:
                conn.execute("CREATE TABLE STUDENTS(NAME VARCHAR(30),REG_NO VARCHAR(20),PROJECT VARCHAR(30),MOBILE VARCHAR(15), EMAIL VARCHAR(30),PASSWORD VARCHAR(30),SUPERVISOR VARCHAR(20), MESSAGE VARCHAR(50))");                 
                content=conn.execute("SELECT NAME,PASSWORD,SUPERVISOR FROM STUDENTS");
            flag =0
            for row in content:
                if(row[0] ==name and row[1]==password):
                    flag=1
                    username=row[0]
                    supera= row[2]
                    break
            if(flag==1):
                conn.close()
                newUser.destroy()
                ReqSupervisor()
            else:
                tkMessageBox.showinfo("Error","Incorrect Password or username!")        
            return
    Login_Now=Button(newUser,width=45,text="Login Now",bg='BLUE',fg='BLACK',command=login_now)
    Login_Now.pack()
    exits = Button(newUser,text="Exit",width=45,bg='RED',fg='WHITE',command=newUser.destroy)
    exits.pack()



                #list of supervisor for student for requesting
def ReqSupervisor():
    global username,supera
    ReqSupervisor=Toplevel(main)
    ReqSupervisor.title("List of Supervisor")
    ls = Listbox(ReqSupervisor,width=55,bg='black',height=3,fg='green',font=("Helvetica", "20"))
    ls.insert(1,"    Hello, "+username)
    if(supera!=''):
        ls.insert(2,"Supervisor already selected!")
        info ="Your supervisor is "+supera
        ls.insert(3,info)
        ls.pack()
    else:
        ls.insert(2,"No Supervisor selected,please select any of them.")
        ls.pack()
        fst= sqlite3.connect('student.db');
        try:
            supe= fst.execute("SELECT NAME,SPECIAL FROM SUPERVISORS");
        except OperationalError:
            conn.execute("CREATE TABLE SUPERVISORS (NAME VARCHAR(30),UID VARCHAR(15),PASSWORD VARCHAR(25),SPECIAL VARCHAR(30),MOBILE VARCHAR(15),EMAIL VARCHAR(30),MESSAGE VARCHAR(50))");    
            supe= fst.execute("SELECT NAME,SPECIAL FROM SUPERVISORS");
        lk = Listbox(ReqSupervisor,width=55,height=2,font=('Helvetica','15'))
        index=0
        for row in supe:
            info= row[0]+ " ( "+row[1]+ " )"
            lk.insert(index,info)
            index += 1
        fst.close()
        lk.pack()
        newsup =Label(ReqSupervisor,text="Name of supervisor",width=30)
        newsup.pack()
        namesup=Entry(ReqSupervisor,width=30)
        namesup.pack()
        def confirms(): 
            if(tkMessageBox.askyesno("confirm","Are You Sure?")):
                conn =sqlite3.connect('student.db')
                try:
                    sups= conn.execute("SELECT NAME FROM SUPERVISORS");
                except OperationalError:
                    conn.execute("CREATE TABLE SUPERVISORS (NAME VARCHAR(30),UID VARCHAR(15),PASSWORD VARCHAR(25),SPECIAL VARCHAR(30),MOBILE VARCHAR(15),EMAIL VARCHAR(30),MESSAGE VARCHAR(50))");
                    sups= conn.execute("SELECT NAME FROM SUPERVISORS");
                flag =0
                for row in sups:
                    if(row[0]==namesup.get()):
                        flag=1
                        break
                if(flag==1):
                    conn.execute("UPDATE STUDENTS SET SUPERVISOR=? WHERE NAME=?;",(namesup.get(),username));
                    tkMessageBox.showinfo("Sucess","Supervisor selected")
                else:
                    tkMessageBox.showinfo("Failure","Supervisor name not matched!")
                conn.commit()
                conn.close()
        confirm = Button(ReqSupervisor,text="select supervisor",width=30,bg="blue",relief="raised",command=confirms)
        confirm.pack()
        #if(tkMessageBox.askyesno("confirm","Are You Sure?")):
            #print "confirm"
    exits = Button(ReqSupervisor,text="Exit",width=22,height=3,bd=3,bg='RED',fg='WHITE',command=ReqSupervisor.destroy)
    exits.pack(side=BOTTOM)



                            #Sign Up for student
def newUser():
    newUser=Toplevel(main)
    newUser.title("New User Student")
    Name = Label(newUser,text="Name",width=45)
    Name.pack()
    NameVal= Entry(newUser,width=45)
    NameVal.pack()
    RegNo = Label(newUser,text="Reg. No",width=45)
    RegNo.pack()
    RegNoval=Entry(newUser,width=45)
    RegNoval.pack()
    Password = Label(newUser,text="Password",width=45)
    Password.pack()
    PassVal=Entry(newUser,show="*",width=45)
    PassVal.pack()
    Specialization = Label(newUser,text="Project Name",width=45)
    Specialization.pack()
    Sepcval=Entry(newUser,width=45)
    Sepcval.pack()
    MobileNo = Label(newUser,text="Mobile No",width=45)
    MobileNo.pack()
    MobVal=Entry(newUser,width=45)
    MobVal.pack()
    EmailId = Label(newUser,text="Email Id",width=45)
    EmailId.pack()
    EmailVal=Entry(newUser,width=45)
    EmailVal.pack()
                            #register function for sign up for student
    def regis():
        name = NameVal.get()
        regno= RegNoval.get()
        project= Sepcval.get()
        Mobi = MobVal.get()
        email= EmailVal.get()
        passval=PassVal.get()
        if(name=='' or regno=='' or project=='' or Mobi=='' or email=='' or passval==''):
            tkMessageBox.showinfo("Missing Value","Enter valid information")
            return
        else:
            conn=sqlite3.connect('student.db');
            #VARCHAR(30),REG_NO VARCHAR(20),PROJECT VARCHAR(30),MOBILE VARCHAR(15), EMAIL VARCHAR(30),PASSWORD VARCHAR(30),MESSAGE
            try:
                conn.execute("INSERT INTO STUDENTS VALUES (?,?,?,?,?,?,?,?);",(name,regno,project,Mobi,email,passval,'',''));
            except OperationalError:
                conn.execute("CREATE TABLE STUDENTS(NAME VARCHAR(30),REG_NO VARCHAR(20),PROJECT VARCHAR(30),MOBILE VARCHAR(15), EMAIL VARCHAR(30),PASSWORD VARCHAR(30),SUPERVISOR VARCHAR(20), MESSAGE VARCHAR(50))"); 
                conn.execute("INSERT INTO STUDENTS VALUES (?,?,?,?,?,?,?,?);",(name,regno,project,Mobi,email,passval,'',''));  
            conn.commit()
            data = conn.execute("SELECT NAME,REG_NO,PROJECT,MOBILE,EMAIL,PASSWORD  from STUDENTS")
            tkMessageBox.showinfo("Success ","Student New User Account Created!")
            newUser.destroy()
            return
    Register=Button(newUser,text="Register",width=45,height=3,bd=3,bg='BLUE',fg='BLACK' ,command=regis)
    Register.pack()
    exits = Button(newUser,text="Exit",width=45,height=3,bd=3,bg='RED',fg='WHITE',command=newUser.destroy)
    exits.pack()

    


                            #SuperVisor page
def Supervisors_page():
    Supervisors_page= Toplevel(main)
    Supervisors_page.title("Supervisor")
    Supervisors_page.minsize(400,100)
    frame=Frame(Supervisors_page)
    frame.pack()
    login = Button(frame,fg='black',width=45,bd=5,bg='BLUE',text='Login',height=5,command=Supervisor_login)
    login.pack()
    New_user=Button(frame,fg='black',width=45,bd=5,bg='BLUE',text='New User',height=5,command=New_Supervisor)
    New_user.pack()
    exits = Button(Supervisors_page,text="Exit",bg='RED',fg='WHITE',width=45,height=5,bd=3,command=Supervisors_page.destroy)
    exits.pack()



                            #Sign in for supervisor
def Supervisor_login():
    Supervisor_login=Toplevel(main)
    Supervisor_login.title("Login Supervisor")
    frame=Frame(Supervisor_login,width=45)
    frame.pack()
    UserName = Label(Supervisor_login,text="User Name",width=45)
    UserName.pack()
    UserNameVal= Entry(Supervisor_login,width=45)
    UserNameVal.pack()
    Password = Label(Supervisor_login,text="Password",width=45)
    Password.pack()
    Passwordval=Entry(Supervisor_login,show="*",width=45)
    Passwordval.pack()
    def sign_in():
        global username
        name=UserNameVal.get()
        password= Passwordval.get()
        if(name=='' or password==''):
            tkMessageBox.showinfo("Missing Value","Username or password empty!")
            return
        else:
            conn = sqlite3.connect('student.db')
            try:
                content=conn.execute("SELECT NAME,PASSWORD FROM SUPERVISORS");
            except OperationalError:
                conn.execute("CREATE TABLE SUPERVISORS (NAME VARCHAR(30),UID VARCHAR(15),PASSWORD VARCHAR(25),SPECIAL VARCHAR(30),MOBILE VARCHAR(15),EMAIL VARCHAR(30),MESSAGE VARCHAR(50))"); 
                content=conn.execute("SELECT NAME,PASSWORD FROM SUPERVISORS");
            flag =0
            for row in content:
                if(row[0] ==name and row[1]==password):
                    flag=1
                    username=row[0]
                    break
            if(flag==1):
                Supervisor_login.destroy()
                select_student()
            else:
                tkMessageBox.showinfo("Error","Incorrect Password or username!")        
            return
        
    Login_Now=Button(Supervisor_login,width=45,bd=3,height=3,text="Login Now",bg='BLUE',fg='BLACK' ,command=sign_in)
    Login_Now.pack()
    exits = Button(Supervisor_login,text="Exit",width=45,bd=3,height=3,bg='RED',fg='WHITE',command=Supervisor_login.destroy)
    exits.pack()
    

                                                #SELECT STUDENT
def select_student():
    global username
    select_students=Toplevel(main)
    select_students.title("Students who selected you")
    ls = Listbox(select_students,width=45)
    ls.insert(1,"Supervisor name: "+username)
    lst= sqlite3.connect('student.db')
    supe= lst.execute("SELECT NAME,PROJECT,SUPERVISOR FROM STUDENTS");
    flag=0
    ls.insert(2,"name (project name)")
    index=3
    for row in supe:
        if(row[2]==username):
            flag=1
            index +=1
            info = row[0]+" ("+row[1]+ " )"
            ls.insert(index,info)
    if(flag==0):
        ls.insert(2,"No item found!")
    ls.pack()
    lst.close()
    exits = Button(select_students,text="Exit",width=22,bg='RED',fg='WHITE',command=select_students.destroy)
    exits.pack()



                        #sign up for new SuperVisor
def New_Supervisor():
    newUser=Toplevel(main)
    newUser.title("New User Supervisor")
    newUser.minsize(400,600)
    newUser.maxsize(400,600)
    Name = Label(newUser,text="Name",width=45)
    Name.pack()
    NameVal= Entry(newUser,width=45)
    NameVal.pack()
    UID = Label(newUser,text="UID",width=45)
    UID.pack()
    UIDval=Entry(newUser,width=45)
    UIDval.pack()
    Password = Label(newUser,text="Password",width=45)
    Password.pack()
    PassVal=Entry(newUser,show="*",width=45)
    PassVal.pack()
    Specialization = Label(newUser,text="Specialization",width=45)
    Specialization.pack()
    Sepcval=Entry(newUser,width=45)
    Sepcval.pack()
    MobileNo = Label(newUser,text="Mobile No",width=45)
    MobileNo.pack()
    MobVal=Entry(newUser,width=45)
    MobVal.pack()
    EmailId = Label(newUser,text="Email Id",width=45)
    EmailId.pack()
    EmailVal=Entry(newUser,width=45)
    EmailVal.pack()
                                            #IMPORTING DATA TO SUPERVISORS
    def regisT():
        name = NameVal.get()
        uid= UIDval.get()
        passw= PassVal.get()
        Speci = Sepcval.get()
        Mobi= MobVal.get()
        Emails=EmailVal.get()
        if(name=='' or uid=='' or passw=='' or Mobi=='' or Emails=='' or Speci==''):
            tkMessageBox.showinfo("Missing Value","Enter valid information")
            return
        else:
            conn=sqlite3.connect('student.db');
            #NAME VARCHAR(30),UID VARCHAR(15),PASSWORD VARCHAR(25),SPECIAL VARCHAR(30),MOBILE VARCHAR(15),EMAIL VARCHAR(30),MESSAGE 
            try:
                conn.execute("INSERT INTO SUPERVISORS VALUES (?,?,?,?,?,?,?);",(name,uid,passw,Speci,Mobi,Emails,''));
            except OperationalError:
                conn.execute("CREATE TABLE SUPERVISORS (NAME VARCHAR(30),UID VARCHAR(15),PASSWORD VARCHAR(25),SPECIAL VARCHAR(30),MOBILE VARCHAR(15),EMAIL VARCHAR(30),MESSAGE VARCHAR(50))"); 
                conn.execute("INSERT INTO SUPERVISORS VALUES (?,?,?,?,?,?,?);",(name,uid,passw,Speci,Mobi,Emails,''));
            conn.commit()
            tkMessageBox.showinfo("Success ","Supervisor account created!")
            newUser.destroy()
            return
    
    
    Register=Button(newUser,text="Register",width=45,height=5,bd=5,bg='BLUE',fg='BLACK',command = regisT)
    Register.pack()
    #(NAME VARCHAR(30),UID VARCHAR(15),PASSWORD VARCHAR(25),SPECIAL VARCHAR(30),MOBILE VARCHAR(15),EMAIL VARCHAR(30))
    exits = Button(newUser,text="Exit",bg='RED',width=45,height=5,bd=5,fg='WHITE',command=newUser.destroy)
    exits.pack()

    
                            #reset funtion
def reset():
    conn=sqlite3.connect('student.db');    
    if(tkMessageBox.askyesno("Delete Student's data",'Are you sure? ')):
        try:
            conn.execute("DELETE  FROM STUDENTS");
        except OperationalError:
            conn.execute("CREATE TABLE STUDENTS(NAME VARCHAR(30),REG_NO VARCHAR(20),PROJECT VARCHAR(30),MOBILE VARCHAR(15), EMAIL VARCHAR(30),PASSWORD VARCHAR(30),SUPERVISOR VARCHAR(20), MESSAGE VARCHAR(50))"); 
        conn.commit()
        tkMessageBox.showinfo("Students Table reset","Your data is now empty")
    if(tkMessageBox.askyesno("Delete Supervisor's data","Are you sure?")):
        try:
            conn.execute("DELETE  FROM SUPERVISORS");
        except OperationalError:
            conn.execute("CREATE TABLE SUPERVISORS (NAME VARCHAR(30),UID VARCHAR(15),PASSWORD VARCHAR(25),SPECIAL VARCHAR(30),MOBILE VARCHAR(15),EMAIL VARCHAR(30),MESSAGE VARCHAR(50))");    
        conn.commit()
        tkMessageBox.showinfo("Supervisor's Table reset","Your data is now empty")
    else:
        tkMessageBox.showinfo("Table reset","Your  required data is now empty")        
    conn.close()
    return


                            #main Function
main= Tk()
main.title("Student")
main.minsize(1066,600)
main.maxsize(1066,600)
frame=Frame(main)
frame.pack()
canvas= Canvas(main,width=1066,height=700)
filename = PhotoImage(file = "coversa.gif")
image = canvas.create_image(1066,0,anchor=NE, image=filename)
login = Button(frame,fg='black',width=30,height=4,bd=5,bg='BLUE',text='Login',command =login)
login.pack(side=LEFT)
New_user=Button(frame,fg='black',width=30,height=4,bd=5,bg='BLUE',text='New User',command=newUser)
New_user.pack(side=LEFT)
Supervisor=Button(frame,fg='black',bd=5,bg='BLUE',width=35,height=4,text='Supervisor Area',command=Supervisors_page)
Supervisor.pack(side=LEFT)
reset = Button(frame,fg='black',width=35,height=4,bd=5,bg='BLUE',text='Reset',command =reset)
reset.pack(side=LEFT)
canvas.pack()
main.mainloop()
