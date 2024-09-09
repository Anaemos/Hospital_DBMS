# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 18:04:45 2023

@author: Aryavart SIngh Payal
"""
import mysql.connector as sqltor
mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127')
mycur=mycon.cursor()
mycur.execute("Create database if not exists hospital")
import mysql.connector as sqltor
mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
mycur=mycon.cursor()


#For sign up and log in (Doctor)--

import mysql.connector as sqltor
mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
mycur=mycon.cursor()
mycur.execute('Create table if not exists Doctor(DoctorId integer primary key, DoctorName varchar(15),DoctorAge smallint unsigned,Department varchar(30),UserName varchar(30),Password integer)')

import mysql.connector as sqltor
mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')

def loginDT():
    x=int(input("Enter the Doctor id"))
    u=input("Enter your user name")
    mycur=mycon.cursor()
    qry="select * from Doctor"
    mycur.execute(qry)
    data=mycur.fetchall()
    for row in data:
        if u in row:
            X1=int(input("Enter the password"))
            if X1 in row:
                 print("You have been succesfully logined")
            else:
                 print("Invalid password")
        elif u not in row:
            print("Invalid Username")
    main_D()

def signinDT():
        x=int(input("Enter the Doctor id"))
        y=input("Enter your Name")
        a=int(input("Enter your age"))
        z=input("Enter your department")
        u=input("Enter your user name")
        P=input("Enter your password")
        mycur=mycon.cursor()
        mycur.execute("Insert into Doctor(DoctorId,DoctorName,DoctorAge,Department,UserName,Password)values({},'{}',{},'{}','{}',{})".format(x,y,a,z,u,P))
        mycon.commit()
        print("You have been succesfully signedup")
        speciality()
        main_D()

#For login and sign up (Patient)--


import mysql.connector as sqltor
mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
mycur=mycon.cursor()
mycur.execute('Create table if not exists Patient(PatientId integer primary key,FirstName varchar(15),LastName varchar(30),age varchar(30),UserName varchar(30),Password integer,Registration_Date Date)')

import mysql.connector as sqltor
mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')

def loginPT():
    x=int(input("Enter the Patient id"))
    u=input("Enter your user name")
    mycur=mycon.cursor()
    qry1="select * from Patient"
    mycur.execute(qry1)
    data=mycur.fetchall()
    for row in data:
        if u in row:
            X1=int(input("Enter the password"))
            if X1 in row:
                 print("You have been succesfully logined")
            else:
                 print("Invalid password")
        elif u not in row:
            print("Invalid Username")
    main_P()
    
def signinPT():
        x1=int(input("Enter the Patient id"))
        y1=input("Enter your First Name")
        a1=input("Enter your Last Name")
        z1=int(input("Enter your age"))
        u1=input("Enter your user name")
        P1=int(input("Enter your password"))
        from datetime import date
        date_components = input('Enter date of admission formatted as YYYY-MM-DD: ').split('-')
        year,month,day = [int(item) for item in date_components]
        d = date(year, month,day)
        mycur=mycon.cursor()
        mycur.execute("Insert into Patient(PatientId,FirstName,LastName,Age,UserName,Password,Registration_Date)values({},'{}','{}',{},'{}',{},'{}')".format(x1,y1,a1,z1,u1,P1,d))
        mycon.commit()
        print("You have been succesfully signedup")
        main_P()

#Speciality(Doctor)--


import mysql.connector as sqltor
mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
mycur=mycon.cursor()
mycur.execute('Create table if not exists spciallity(DoctorId integer primary key,Speciality varchar(30))')


def speciality():
    DI=int(input("Enter your doctor id "))
    Sp=input("Enter your speciality")
    Qry2="Select DoctorId from doctor"
    mycur.execute(Qry2)
    Data1=mycur.fetchall()
    for item in Data1:
        if item==DI:
            mycur.execute("Insert into Speciality(DoctorId,Speciality)values('{}','{}')".format(D1,Sp))
        else:
            print("Invalid User")
    main_D()

#Appointment Table -->
    
import mysql.connector as sqltor
mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
mycur=mycon.cursor()
mycur.execute('''CREATE TABLE IF NOT EXISTS appointments(
                    id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    patient_id INTEGER,
                    appointment_date TEXT NOT NULL,
                    FOREIGN KEY (patient_id) REFERENCES patient(patientid))''')
    
#To add new doctor id -->

def add_doctor_id():
    ID=input("Enter the doctor ID")
    Password=input("Enter the password")
    import mysql.connector as sqltor
    mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
    mycur=mycon.cursor()
    Q=mycur.execute("select username,password from doctor")
    Data=mycur.fetchall()
    for row in data:
        if (ID,Password)==row:
            print("Doctor id already registered")
        else:
            signinDT()
    main_D()

#To add new patient id -->

def add_patient_id():
    ID=input("Enter the patient ID")
    Password=input("Enter the password")
    import mysql.connector as sqltor
    mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
    mycur=mycon.cursor()
    Q=mycur.execute("select username,password from patient")
    Data=mycur.fetchall()
    for row in Data:
        if (ID,Password)==row:
            print("Patient already admitted")
        else:
            print("Please add the details of new patient")
            signinPT()
    main_D()
    
#To delete a doctor id -->

def del_doctor_id():
    ID=input("Enter the doctor id")
    Query="delete from doctor where DoctorId = %s,(ID)"
    import mysql.connector as sqltor
    mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
    mycur=mycon.cursor()
    mycur.execute(Query)
    mycon.commit()
    main_D()

#To delete a patient id -->

def del_patient_id():
    ID=input("Enter the patient id")
    Query="delete from doctor where PatientId = %s,(ID)"
    import mysql.connector as sqltor
    mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
    mycur=mycon.cursor()
    mycur.execute(Query)
    mycon.commit()
    main_D()


#To search for doctor details-->

def searchDT():
    ID = input("Enter the doctor ID")
    import mysql.connector as sqltor
    mycon = sqltor.connect(user='root', host='localhost', password='JohnWick3127', database='hospital1')
    mycur = mycon.cursor()
    mycur.execute("select * from doctor where doctorID = %s", (ID,))
    data = mycur.fetchall()
    if data:
        for row in data:
            print(row)  # Display the fetched data
    else:
        print("Doctor not found with this ID")
    main_P()
    """ID=input("Enter the doctor ID")
    import mysql.connector as sqltor
    mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
    mycur=mycon.cursor()
    Q=mycur.execute("select username from doctor")
    data=mycur.fetchall()
    for row in data:
        if (ID)==row:
            mycur.execute("select * from doctor where doctorID = ID")
            print(mycur.fetchall())
    main_P()"""

#To search for patient details--

def searchPT():
    ID=input("Enter the doctor ID")
    import mysql.connector as sqltor
    mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
    mycur=mycon.cursor()
    Q=mycur.execute("select username from patient")
    Data=mycur.fetchall()
    for row in data:
        if (ID)==row:
            mycur.execute("select * from patient where patientID = ID")
            print(mycur.fetchall())
    main_D()

#To see details of all the doctors--

def displayDT():
    sql="Select*from doctor"
    import mysql.connector as sqltor
    mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
    mycur=mycon.cursor()
    Q=mycur.execute("select * from doctor")
    myresult=mycur.fetchall()
    for i in myresult:
        print("DoctorId:\t",i[0])
        print("DoctorName:\t",i[1])
        print("DoctorAge:\t",i[2])
        print("Department:\t",i[3])
        print(">==============================================================================<")
    main()

#To see the details of all the patients--

def displayPT():
    sql="Select*from patient"
    import mysql.connector as sqltor
    mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
    mycur=mycon.cursor()
    Q=mycur.execute("select * from patient")
    myresult=mycur.fetchall()
    for i in myresult:
        print("PatientId:\t",i[0])
        print("First Name:\t",i[1])
        print("Last Name:\t",i[2])
        print("Patient age:\t",i[3])
        print(">==============================================================================<")

    main_D()
              

# Appointment --->>


def schedule_appointment():
            patient_id=int(input("Enter the patient ID"))
            from datetime import date
            date_components = input('Enter date of Appointment formatted as YYYY-MM-DD: ').split('-')
            year,month,day = [int(item) for item in date_components]
            Appointment_Date = date(year, month,day)
            import mysql.connector as sqltor
            mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
            mycur = mycon.cursor()
            mycur.execute('Create table if not exists Appointment(patient_id int primary key,Appointment_Date date)')
            mycur.execute('INSERT INTO Appointment(patient_id,Appointment_Date)VALUES(%s,"%s")'.format(patient_id,str(Appointment_Date)))
            main_P()

def get_patient_appointments():
            patient_id=int(input("Enter the patient ID"))
            import mysql.connector as sqltor
            mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
            mycur = mycon.cursor()
            mycur.execute('SELECT * FROM appointments WHERE patient_id = ?', (patient_id))
            appointments = mycur.fetchall()
            return appointments
            main_P()

# Diagnosis -->>

def add_diagnosis():
        appointment_id=int(input("Enter the appointment_id"))
        diagnosis_text=input("Enter the diagnosis")
        import mysql.connector as sqltor
        mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
        mycur = mycon.cursor()
        mycur.execute('Create table if not exists diagnosis(appointment_id int primary key,diagnosis_text varchar(20))')
        mycur.execute('INSERT INTO diagnosis(appointment_id, diagnosis_text)VALUES(?, ?)'.format(appointment_id, diagnosis_text))
        main_P()

# Bill --


def generate_bill():
        Appointment_ID=int(input("Enter the appointment id"))
        Amount=int(input("Enter the amount"))
        import mysql.connector as sqltor
        mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
        mycur = mycon.cursor()
        mycur.execute('Create table if not exists bills(Appointment_ID int primary key,Amount integer)')
        mycur.execute("Insert into bills(Appointment_ID,Amount)values({},{})".format(Appointment_ID,Amount))
        main_D()

def View_bill():
        ID=int(input("Enter the appointment id"))
        import mysql.connector as sqltor
        mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
        mycur = mycon.cursor()
        try:
            Query="Select* from bills where Appointment_ID=ID"
            mycur.execute(Query)
            data=mycur.fetchall()
            print(data)
        except OperationalError:
            print("No appointment had taken place")
        main_P()

# Fee Structure -->>

def add_service_fee():
            service_name=input("Enter the service_name")
            fee_amount=int(input("Enter the fee_amount"))
            import mysql.connector as sqltor
            mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
            mycur = mycon.cursor()
            mycur.execute('Create table if not exists fee_structure(service_name varchar(40),fee_amount int)')
            mycur.execute('INSERT INTO fee_structure(service_name, fee_amount) VALUES (?, ?)',(service_name, fee_amount))
            main_D()

def get_fee_structure():
       import mysql.connector as sqltor
       mycon=sqltor.connect(user='root',host='localhost',password='JohnWick3127',database='hospital1')
       mycur = mycon.cursor()
       mycur.execute('SELECT * FROM fee_structure')
       fee_structure = cursor.fetchall()
       return fee_structure
       main_P()
    

## Dash Board ---->>


from tkinter import *
main = Tk()
ourMessage ='Welcome to HOSPITAL DBMS'
messageVar = Message(main, text = ourMessage)
messageVar.config(bg='white',width='1500')
messageVar.pack( )
main.mainloop( )

def main_D():
                        print("""Please select the specified options -->
                          1. Log-In
                          2. Sign-In
                          3. Speciality
                          4. Add new Doctor ID
                          5. Delete excisting Doctor ID
                          6. Add new Patient ID
                          7. To display all the Details of Doctors
                          8. To display all the Details of Patients
                          9. Search for Patient Details
                         10. To add bill
                         11. To add fee structure
                         12. Exit""")
                        choice=input("Enter your choice \n(1/2/3/4/5/6/7/8/9/10/11/12):")
                        if choice == '1':
                            loginDT()
                            
                        elif choice == "2":
                            signinDT()
                            
                        elif choice == "3":
                            speciality()
                            
                        elif choice == "4":
                            add_doctor_id()
                            
                        elif choice == "5":
                            del_doctor_id()
                            
                        elif choice == "6":
                            add_patient_id()
                            
                        elif choice == "7":
                            displayDT()
                            
                        elif choice == "8":
                            displayPT()
                            
                        elif choice == "9":
                            searchPT()

                        elif choice=="10":
                            generate_bill()

                        elif choice=="11":
                            add_service_fee()
                            
                        elif choice == "12":
                            print(" Work Done !! Thank you ")

                        else:
                           print("try again /n Please Enter correct choice")
                           main_D()

def main_P():
                        print("""Please select the specified options -->
                          1. Log-In
                          2. Sign-In
                          3. Search for Doctor Details
                          4. To display all the Details of Doctors
                          5. To set appointment with Doctor
                          6. Diagnosis
                          7. To get Fee Structure
                          8. View_bill
                          9. Exit""")
                        choice=input("Enter your choice \n(1/2/3/4/5/6/7/8/9):")
                        if choice == '1':
                            loginPT()
                            
                        elif choice == "2":
                            signinPT()
                            
                        elif choice == "3":
                            searchDT()
                            
                        elif choice == "4":
                            displayDT()
                            
                        elif choice == "5":
                            N=input("""To shedule Appointment - 1
                                           To get Appointment - 2""")
                            if N == "1":
                                schedule_appointment()
                            elif N == "2":
                                get_patient_appointments()
                                
                        elif choice == "6":
                            add_diagnosis()
                            
                        elif choice == "7":
                            generate_bill()
                            
                        elif choice == "8":
                            get_fee_structure()
                            
                        elif choice == "9":
                            print(" Work Done !! Thank you ")
                            
                        else:
                           print("try again /n Please Enter correct choice")
                           main_P()

def main():
    print("""=============================================================HOSPITAL DBMS===================================================================""")
    Option=print("""Dear user please select your designation
                    Doctor - D or Patient - P""")
    Designation =input("Enter your designation")
    if str(Designation).upper() == "D":
                        main = Tk()
                        ourMessage ='''Wherever the art of medicine is loved, there is also a love of humanity.'''
                        messageVar = Message(main, text = ourMessage)
                        messageVar.config(bg='white',width='1500')
                        messageVar.pack( )
                        main.mainloop( )
                        main_D()
    elif str(Designation).upper() == "P":
                        main = Tk()
                        ourMessage ='''Dear Patient , We are delighted to welcome you! Our team is committed to providing
                        exceptional healthcare and ensuring your well-being. To help you get started, we have
                        enclosed a new patient registration form and a list of our services'''
                        messageVar = Message(main, text = ourMessage)
                        messageVar.config(bg='white',width='1500')
                        messageVar.pack( )
                        main.mainloop( )
                        main_P()
main_P()
