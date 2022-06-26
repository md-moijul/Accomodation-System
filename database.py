import sqlite3
from tkinter import *
from PIL import ImageTk,Image



conn = sqlite3.connect('login.db')
c = conn.cursor()




def create_table():
    c.execute("""CREATE TABLE login_info (
		email text,
		password text,
        type text
		)""")

def data_entry(): 
    c.execute("INSERT INTO login_info VALUES('wisalh@gmail.com','1900011','student')")
    c.execute("INSERT INTO login_info VALUES('jhonmc@live.com','1900022','student')")
    c.execute("INSERT INTO login_info VALUES('abdo@yahoo.com','1900033', 'student')")
    c.execute("INSERT INTO login_info VALUES('moonlight@gmail.com','1900044', 'studen')")
    c.execute("INSERT INTO login_info VALUES('ajtheman@gmail.com','1900055', 'student')")
    c.execute("INSERT INTO login_info VALUES('Jen.Leric@hotmail.com','horfield420', 'warden')")
    c.execute("INSERT INTO login_info VALUES('AlfieD1989@live.com','password', 'warden')")
    c.execute("INSERT INTO login_info VALUES('jimbobace@gmail.com','kevinhart', 'warden')")
    c.execute("INSERT INTO login_info VALUES('felixthecat@gmail.com','managerbigman' , 'manager')")

create_table()
data_entry()
for row in c.execute("SELECT * FROM login_info"):
    print(row)



def create_table():
    c.execute('CREATE TABLE student(StudentNumber INTEGER NOT NULL PRIMARY KEY, StudentName TEXT, StudentPhoneNumber INTEGER, StudentEmail TEXT, ApplicationStatus TEXT)')

def data_entry():
   c.execute("INSERT INTO student VALUES(190001, 'Wissam Salhab', 0582777200, 'wisalh@gmail.com','Accepted')")
   c.execute("INSERT INTO student VALUES(190002, 'John McCarrey', 4478569235, 'jhonmc@live.com','Accepted')")
   c.execute("INSERT INTO student VALUES(190003, 'Abdulaziz hallab', 4123986512, 'abdo@yahoo.com','Pending')")
   c.execute("INSERT INTO student VALUES(190004, 'Omar Monla', 4435698745, 'moonlight@gmail.com','Accepted')")
   c.execute("INSERT INTO student VALUES(190005, 'ajay tracey', 4478569854, 'ajtheman@gmail.com','Accepted')")   

create_table()
data_entry()
for row in c.execute("SELECT * FROM student"):
    print(row)


def create_table():
    c.execute('CREATE TABLE rentalAgreement(LeaseNumber INTEGER NOT NULL PRIMARY KEY, Rent REAL, LeaseDuration TEXT)')

def data_entry():
   c.execute("INSERT INTO rentalAgreement VALUES(145, 520, '12Months')")
   c.execute("INSERT INTO rentalAgreement VALUES(146, 550, '12Months')")
   c.execute("INSERT INTO rentalAgreement VALUES(147, 900, '24Months')")
   c.execute("INSERT INTO rentalAgreement VALUES(148, 675, '6Months')")
   c.execute("INSERT INTO rentalAgreement VALUES(149, 420, '24Months')")

create_table()
data_entry()
for row in c.execute("SELECT * FROM rentalAgreement"):
    print(row)




def create_table():
    c.execute('CREATE TABLE warden(WardenName TEXT, WardenAddress TEXT, WardenEmail TEXT NOT NULL PRIMARY KEY, WardenNumber INTEGER)')

def data_entry():
   c.execute("INSERT INTO warden VALUES('Jen Leric', 'Horfield', 'Jen.Leric@hotmail.com', 54686549 )")
   c.execute("INSERT INTO warden VALUES('Alfie Davis', 'Hanham', 'AlfieD1989@live.com', 7854986)")
   c.execute("INSERT INTO warden VALUES('Jimbob bob', 'filton', 'jimbobace@gmail.com',74589656)")

create_table()
data_entry()
for row in c.execute("SELECT * FROM warden"):
    print(row)




def create_table():
    c.execute('CREATE TABLE hallManager(ManagerName TEXT,ManagerAddress TEXT, ManagerEmail TEXT, ManagerNumber INTEGER, EditRoomDetails TEXT, ReviewApplication TEXT)')

def data_entry():
   c.execute("INSERT INTO hallManager VALUES('Felix Brown', 'Emersons Green', 'felixthecat@gmail.com', 78549611,' ',' ')")
   c.execute("INSERT INTO hallManager VALUES('MD Moijul', 'Dursley', 'moijul@gmail.com', 78549611,' ',' ')")
   c.execute("INSERT INTO hallManager VALUES('jk', 'Dursley', 'jk.com', 78549611,' ',' ')")

create_table()
data_entry()
for row in c.execute("SELECT * FROM hallManager"):
    print(row)





def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS rooms(RoomNumber INTEGER NOT NULL PRIMARY KEY, Hall TEXT,StudentName TEXT,Studentnumber INTEGER, lease REAL, OccupancyStatus TEXT, CheckRoomClean TEXT, CheckRoomMaintenance TEXT)')

def data_entry(): 
   c.execute("INSERT INTO rooms VALUES(1, 'Brecon','Wissam Salhab',190001, 520, 'Occupied', 'Clean','Good')")
   c.execute("INSERT INTO rooms VALUES(2, 'Jameson',null , null ,550, 'empty', 'Clean','good')")
   c.execute("INSERT INTO rooms VALUES(3, 'Brecon', 'Omar Monla', 190004 , 900, 'Occupied', 'Not Clean','bad')")
   c.execute("INSERT INTO rooms VALUES(4, 'Brecon', null  , null  , 675, 'empty', 'Not Clean','good')")
   c.execute("INSERT INTO rooms VALUES(5, 'Costwold','Ajay tracey', 190005, 420, 'Occupied', 'Clean','good')")

create_table()
data_entry()
for row in c.execute("SELECT * FROM rooms"):
    print(row)


def create_table():
    c.execute('CREATE TABLE accommodationOffice(AvailableRooms INTEGER)')

def data_entry():  
   c.execute("INSERT INTO accommodationOffice VALUES(2)")
   c.execute("INSERT INTO accommodationOffice VALUES(4)")


create_table()
data_entry()
for row in c.execute("SELECT * FROM accommodationOffice"):
    print(row)



conn.commit()
conn.close()

