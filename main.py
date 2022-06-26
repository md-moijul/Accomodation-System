from tkinter import *
import sqlite3
import copy


root = Tk()
root.title('uwesoft')
root.geometry("600x800")


conn = sqlite3.connect('login.db')
c = conn.cursor()



def open_reg():
        top = Toplevel()
        top.title('registration window')
        top.geometry("600x600")
        clicked =StringVar()
        clicked.set("student")
        
        

        conn = sqlite3.connect('login.db')
        c = conn.cursor()

        info = Label(top, text= "enter your details").grid(row=0,column=0)

        e_name_label = Label(top, text="fullname").grid(row=1, column=0, pady=(10, 0))
        e_name_entry = Entry(top, width=30).grid(row=1, column=1, padx=20, pady=(10, 0))
        
        e_dddress_label = Label(top, text="full address").grid(row=2, column=0, pady=(10, 0))
        e_address_entry = Entry(top, width=30).grid(row=2, column=1, padx=20, pady=(10, 0))
        
        e_number_label = Label(top, text="contact number").grid(row=3, column=0, pady=(10, 0))
        e_number_entry = Entry(top, width=30).grid(row=3, column=1, padx=20, pady=(10, 0))
        
        e_email_label = Label(top, text="email").grid(row=4, column=0, pady=(10, 0))
        e_email_entry = Entry(top, width=30).grid(row=4, column=1, padx=20, pady=(10, 0))
        
        e_password_label = Label(top, text="password").grid(row=5, column=0, pady=(10, 0))
        e_password_entry = Entry(top, width=30).grid(row=5, column=1, padx=20, pady=(10, 0))
        
        e_type = Label(top, text="register as :").grid(row=6, column=0, pady=(10, 0))
        drop= OptionMenu(top, clicked, "manager","warden","student").grid(row=6, column=1, pady=(10, 0))
        
        e_register_button= Button(top, text="apply",padx=10, pady= 15,).grid(row=19,column=0,columnspan=3)
        e_exit = Button(top, text="close window", command=top.destroy).grid(row=20,column=0)
        
        
        c.execute("INSERT INTO details VALUES (:name, :address, :number, :email, :password)",
			{
            'name': e_name_entry.get(),
            'address': e_address_entry.get(),
            'number': e_number_entry.get(),
            'email': e_email_entry.get(),
            'password': e_password_entry.get()
            })
        

        conn.commit()
        conn.close()
        
        e_exit = Button(top, text="close window", command=top.destroy).grid(row=20,column=0)

def open_manager():
        top_1 = Toplevel()
        top_1.title('manager\'s window')
        top_1.geometry("600x800")

        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        
        '''
        for row in c.execute("SELECT * FROM hallManager WHERE ManagerEmail =" + profile ):
            profile_name = str(row[0])
        m_welcome_label = Label(top_1, text= "welcome mr " + profile_name).grid(row=0,column=0)
        '''
            
            
        m_frame = LabelFrame(top_1,borderwidth = 5, padx=50, pady=50)
        m_frame.grid(row=1, column=0,columnspan=6, padx=10, pady=10)

        for row in c.execute("SELECT * FROM rooms "):
            room_details = row
        
        
        m_room_num_label = Label(m_frame,relief="solid", text= "room Number").grid(row=0,column=0)
        m_hall_name_label = Label(m_frame,relief="solid", text= "hall names").grid(row=0,column=1)
        m_student_name_label = Label(m_frame,relief="solid", text= "student name").grid(row=0,column=2)
        m_lease_label = Label(m_frame,relief="solid", text= "lease Number").grid(row=0,column=3)
        m_occupency_label = Label(m_frame,relief="solid", text= "occupency status").grid(row=0,column=4)
        m_clean_label = Label(m_frame,relief="solid", text= "cleaning status").grid(row=0,column=5)
        
        c.execute("SELECT * FROM rooms")
        records = c.fetchall()
        
        room_num=int
        hall_name=str
        student_name=str
        lease=int
        occupency=str
        cleaning=str  
        
        new_row = 1 
        for record in records:
            

            m_room_num_label = Label(m_frame,relief="groove", text= (record[0])).grid(row=new_row,column=0)
            m_hall_name_label = Label(m_frame,relief="groove" ,text= (record[1])).grid(row=new_row,column=1)
            m_student_name_label = Label(m_frame,relief="groove", text= (record[2])).grid(row=new_row,column=2)
            m_lease_label = Label(m_frame,relief="groove", text= (record[4])).grid(row=new_row,column=3)
            m_occupency_label = Label(m_frame,relief="groove", text= (record[5])).grid(row=new_row,column=4)
            m_clean_label = Label(m_frame,relief="groove", text= (record[6])).grid(row=new_row,column=5)
            new_row +=1
        
        def get_room_num():
            x_room_num = str(m_edit_entry.get())
            global x_clicked 
            x_clicked = True
            return(x_room_num)
        
        def submit_details():
            print(2)
            conn = sqlite3.connect('login.db')
            c = conn.cursor()
            x_room_num=get_room_num()
            
            c.execute("SELECT * FROM rooms where RoomNumber = " + x_room_num)
            room_records = c.fetchall()
            
            c.execute("""UPDATE rooms SET
                RoomNumber = :room_num,
                Hall = :hall,
                StudentName = :student,
                lease = :lease,
                OccupancyStatus = :occupency,
                CheckRoomClean = :cleaning 
                WHERE RoomNumber= :x_room_num""",
                {
                'room_num': room_num_entry.get(),
                'hall': hall_name_entry.get(),
                'student': student_name_entry.get(),
                'lease': lease_entry.get(),
                'occupency': occupency_entry.get(),
                'cleaning': cleaning_entry.get(),
                'x_room_num': x_room_num
                })
            
            conn.commit()
            conn.close()
        
        
        def edit_room():
            
            conn = sqlite3.connect('login.db')
            c = conn.cursor()
            x_room_num=get_room_num()
            
            c.execute("SELECT * FROM rooms where RoomNumber = " + x_room_num)
            records = c.fetchall()
            
            if x_clicked == True:
                for record in records:
                    room_num_entry.insert(0, record[0])
                    hall_name_entry.insert(0, record[1])
                    student_name_entry.insert(0, record[2])
                    lease_entry.insert(0, record[4])
                    occupency_entry.insert(0, record[5])
                    cleaning_entry.insert(0, record[6])
            
            conn.commit()
            conn.close()
            
            
            
    
            
        global m_edit_entry
        global room_num_entry
        global hall_name_entry
        global student_name_entry
        global lease_entry
        global occupency_entry
        global cleaning_entry
        m_info = Label(top_1, text="change details of room number :").grid(row=2, column=0)
        m_edit_entry = Entry(top_1, width=10)
        m_edit_entry.grid(row=2, column=1, padx=20) 
        m_button = Button(top_1, text="submit", command= edit_room).grid(row=2, column=2, padx=20) 
        
          
        m_frame1 = LabelFrame(top_1,borderwidth = 5, padx=50, pady=50)
        m_frame1.grid(row=3, column=0,columnspan=6, padx=10, pady=10)      

        room_num_label = Label(m_frame1, text="room number :").grid(row=1, column=0, pady=(10, 0))
        room_num_entry = Entry(m_frame1, width=30)
        room_num_entry.grid(row=1, column=1, padx=20, pady=(10, 0))
        
        hall_name_label = Label(m_frame1, text="hall name :").grid(row=2, column=0, pady=(10, 0))
        hall_name_entry = Entry(m_frame1, width=30)
        hall_name_entry.grid(row=2, column=1, padx=20, pady=(10, 0))
        
        student_name_label = Label(m_frame1, text="student name :").grid(row=3, column=0, pady=(10, 0))
        student_name_entry = Entry(m_frame1, width=30)
        student_name_entry.grid(row=3, column=1, padx=20, pady=(10, 0))
        
        lease_label = Label(m_frame1, text="lease number :").grid(row=4, column=0, pady=(10, 0))
        lease_entry = Entry(m_frame1, width=30)
        lease_entry.grid(row=4, column=1, padx=20, pady=(10, 0))
        
        occupency_label = Label(m_frame1, text="occupency status :").grid(row=5, column=0, pady=(10, 0))
        occupency_entry = Entry(m_frame1, width=30)
        occupency_entry.grid(row=5, column=1, padx=20, pady=(10, 0))
        
        cleaning_label = Label(m_frame1, text="cleaning status :").grid(row=6, column=0, pady=(10, 0))
        cleaning_entry = Entry(m_frame1, width=30)
        cleaning_entry.grid(row=6, column=1, padx=20, pady=(10, 0))
        
        m_submit_button = Button(m_frame1, text="submit", command= submit_details).grid(row=7, column=1, padx=20) 
        m_logout_button = Button(top_1, text="logout", command=top_1.destroy).grid(row=7, column=1, padx=20) 
     
       
 
    
        
        
        conn.commit()
        conn.close()

def open_warden():
        top_1 = Toplevel()
        top_1.title('warden\'s window')
        top_1.geometry("600x800")

        conn = sqlite3.connect('login.db')
        c = conn.cursor()
            
            
        m_frame = LabelFrame(top_1,borderwidth = 5, padx=50, pady=50)
        m_frame.grid(row=1, column=0,columnspan=6, padx=10, pady=10)

        for row in c.execute("SELECT * FROM rooms "):
            room_details = row
        
        
        m_room_num_label = Label(m_frame,relief="solid", text= "room Number").grid(row=0,column=0)
        m_hall_name_label = Label(m_frame,relief="solid", text= "hall names").grid(row=0,column=1)
        m_student_name_label = Label(m_frame,relief="solid", text= "student name").grid(row=0,column=2)
        m_lease_label = Label(m_frame,relief="solid", text= "lease Number").grid(row=0,column=3)
        m_occupency_label = Label(m_frame,relief="solid", text= "occupency status").grid(row=0,column=4)
        m_clean_label = Label(m_frame,relief="solid", text= "cleaning status").grid(row=0,column=5)
        
        c.execute("SELECT * FROM rooms")
        records = c.fetchall()
        
        room_num=int
        hall_name=str
        student_name=str
        lease=int
        occupency=str
        cleaning=str  
        
        new_row = 1 
        for record in records:
            

            m_room_num_label = Label(m_frame,relief="groove", text= (record[0])).grid(row=new_row,column=0)
            m_hall_name_label = Label(m_frame,relief="groove" ,text= (record[1])).grid(row=new_row,column=1)
            m_student_name_label = Label(m_frame,relief="groove", text= (record[2])).grid(row=new_row,column=2)
            m_lease_label = Label(m_frame,relief="groove", text= (record[4])).grid(row=new_row,column=3)
            m_occupency_label = Label(m_frame,relief="groove", text= (record[5])).grid(row=new_row,column=4)
            m_clean_label = Label(m_frame,relief="groove", text= (record[6])).grid(row=new_row,column=5)
            new_row +=1
        
        def get_room_num():
            x_room_num = str(m_edit_entry.get())
            global x_clicked 
            x_clicked = True
            return(x_room_num)
        
        def submit_details():
            print(2)
            conn = sqlite3.connect('login.db')
            c = conn.cursor()
            x_room_num=get_room_num()
            
            c.execute("SELECT * FROM rooms where RoomNumber = " + x_room_num)
            room_records = c.fetchall()
            
            c.execute("""UPDATE rooms SET
                RoomNumber = :room_num,
                Hall = :hall,
                StudentName = :student,
                lease = :lease,
                OccupancyStatus = :occupency,
                CheckRoomClean = :cleaning 
                WHERE RoomNumber= :x_room_num""",
                {
                'room_num': room_num_entry.get(),
                'hall': hall_name_entry.get(),
                'student': student_name_entry.get(),
                'lease': lease_entry.get(),
                'occupency': occupency_entry.get(),
                'cleaning': cleaning_entry.get(),
                'x_room_num': x_room_num
                })
            
            conn.commit()
            conn.close()
        
        
        def edit_room():
            
            conn = sqlite3.connect('login.db')
            c = conn.cursor()
            x_room_num=get_room_num()
            
            c.execute("SELECT * FROM rooms where RoomNumber = " + x_room_num)
            records = c.fetchall()
            
            if x_clicked == True:
                for record in records:
                    room_num_entry.insert(0, record[0])
                    hall_name_entry.insert(0, record[1])
                    student_name_entry.insert(0, record[2])
                    lease_entry.insert(0, record[4])
                    occupency_entry.insert(0, record[5])
                    cleaning_entry.insert(0, record[6])
            
            conn.commit()
            conn.close()
            
            
            
    
            
        global m_edit_entry
        global room_num_entry
        global hall_name_entry
        global student_name_entry
        global lease_entry
        global occupency_entry
        global cleaning_entry
        m_info = Label(top_1, text="change details of room number :").grid(row=2, column=0)
        m_edit_entry = Entry(top_1, width=10)
        m_edit_entry.grid(row=2, column=1, padx=20) 
        m_button = Button(top_1, text="submit", command= edit_room).grid(row=2, column=2, padx=20) 
        
          
        m_frame1 = LabelFrame(top_1,borderwidth = 5, padx=50, pady=50)
        m_frame1.grid(row=3, column=0,columnspan=6, padx=10, pady=10)      

        room_num_label = Label(m_frame1, text="room number :").grid(row=1, column=0, pady=(10, 0))
        room_num_entry = Entry(m_frame1, width=30 ,state=DISABLED)
        room_num_entry.grid(row=1, column=1, padx=20, pady=(10, 0))
        
        hall_name_label = Label(m_frame1, text="hall name :").grid(row=2, column=0, pady=(10, 0))
        hall_name_entry = Entry(m_frame1, width=30 ,state=DISABLED)
        hall_name_entry.grid(row=2, column=1, padx=20, pady=(10, 0))
        
        student_name_label = Label(m_frame1, text="student name :").grid(row=3, column=0, pady=(10, 0))
        student_name_entry = Entry(m_frame1, width=30,state=DISABLED)
        student_name_entry.grid(row=3, column=1, padx=20, pady=(10, 0))
        
        lease_label = Label(m_frame1, text="lease number :").grid(row=4, column=0, pady=(10, 0))
        lease_entry = Entry(m_frame1, width=30,state=DISABLED)
        lease_entry.grid(row=4, column=1, padx=20, pady=(10, 0))
        
        occupency_label = Label(m_frame1, text="occupency status :").grid(row=5, column=0, pady=(10, 0))
        occupency_entry = Entry(m_frame1, width=30 ,state=DISABLED)
        occupency_entry.grid(row=5, column=1, padx=20, pady=(10, 0))
        
        cleaning_label = Label(m_frame1, text="cleaning status :").grid(row=6, column=0, pady=(10, 0))
        cleaning_entry = Entry(m_frame1, width=30)
        cleaning_entry.grid(row=6, column=1, padx=20, pady=(10, 0))
        
        m_submit_button = Button(m_frame1, text="submit", command= submit_details).grid(row=7, column=1, padx=20) 
        m_logout_button = Button(top_1, text="logout", command=top_1.destroy).grid(row=7, column=1, padx=20) 
     
       
 
    
        
        
        conn.commit()
        conn.close()


def open_student():
        top_1 = Toplevel()
        top_1.title('student\'s window')
        top_1.geometry("600x800")

        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        
        x_email = (str("\'") +str(email_entry.get())+ str("\'"))
        
        for row_info in c.execute("SELECT * FROM student WHERE StudentEmail =" + x_email ):
            print(row_info)
        
        m_frame = LabelFrame(top_1,borderwidth = 5, padx=50, pady=50)
        m_frame.grid(row=1, column=0,columnspan=6, padx=10, pady=10)
        
        s_name_label = Label(m_frame, text="name :" + str(row_info[1])).grid(row=1, column=0, pady=(10, 0))
        s_std_num_label = Label(m_frame, text="student number :" + str(row_info[0])).grid(row=2, column=0, pady=(10, 0))
        s_email_label = Label(m_frame, text="email :" + str(row_info[3])).grid(row=3, column=0, pady=(10, 0))
        s_phone_label = Label(m_frame, text="contact number :" + str(row_info[2])).grid(row=4, column=0, pady=(10, 0))
        s_status_label = Label(m_frame, text="application status  :" + str(row_info[4])).grid(row=5, column=0, pady=(10, 0))
              
        
        conn.commit()
        conn.close()


def login_verification():
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    print(email_entry.get())
    x_email = (str("\'") +str(email_entry.get())+ str("\'"))
    print(x_email)
    x_pass = str(password_entry.get())
    y_pass = str
    global y_access
    
    for row in c.execute("SELECT * FROM login_info where email = " + x_email):
        y_pass=str(row[1])
        y_access = row[2]

    
    
    if x_pass == y_pass :
        print("welcome")


        if y_access == "manager":
            open_manager()
        elif y_access == "warden":
            open_warden()
        elif y_access== "student":
            open_student()
    else :
        print("access denied")
        
        
    conn.commit()
    conn.close()




welcome_label =Label(root, text="welcome to uwesoft") 
welcome_label.grid(row=0,column=0,columnspan=6)

frame = LabelFrame(root,borderwidth = 1, padx=50, pady=50)
frame.grid(row=2, column=0,columnspan=6, padx=10, pady=10)

info = Label(frame, text="enter your login details : ").grid(row=0, column=0)

global email_entry
global password_entry
global clicked

email_label = Label(frame, text="email").grid(row=1, column=0, pady=(10, 0))
email_entry = Entry(frame, width=30)
email_entry.grid(row=1, column=1, padx=20, pady=(10, 0))
password_label = Label(frame, text="password").grid(row=2, column=0, pady=(10, 0))
password_entry = Entry(frame, width=30)
password_entry.grid(row=2, column=1, padx=20, pady=(10, 0))

login_button= Button(frame, text="login",padx=10, pady= 15, command=login_verification).grid(row=1,column=3,rowspan=2)
info2 = Label(frame, text="...or register here :").grid(row=5, column=0,pady=10)
register_button= Button(frame, text="register as new",command= open_reg, padx=10).grid(row=5,column=1)




conn.commit()
conn.close()


root.mainloop()