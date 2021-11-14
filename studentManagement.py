import sqlite3

conn=sqlite3.connect("Student_db")

c=conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS student_info(
                roll integer PRIMARY KEY,
                name text,
                email text,
                gender text,
                phone interger,
                branch text
                )""")

while True:
    print("1. Add student record ")
    print("2. Display all student record ")
    print("3. Display record by roll no ")
    print("4. Edit student record by roll no ")
    print("5. Delete student record by roll no ")
    print("6. Exit ")

    choice = int(input("Enter choice: "))

    if choice ==1:
        roll=int(input("Enter your Roll no : "))
        name=(input("Enter your Name : "))
        email=(input("Enter your Email Id : "))
        gender=(input("Enter your Gender : "))
        phone=int(input("Enter your Phone No : "))
        branch=(input("Enter your Branch : "))

        c.execute("""INSERT INTO student_info VALUES
        (:roll, :name, :email, :gender, :phone, :branch)""",
        {'roll':roll, 'name':name, 'email':email, 'gender':gender, 'phone':phone, 'branch':branch})

        print("Your data is inserted successfully...")


    elif choice==2:
        c.execute("SELECT * FROM student_info")

        print(c.fetchall())

    elif choice==3:
        en_roll=int(input("Enter Roll No: "))
        c.execute("SELECT * FROM student_info WHERE roll={}".format(en_roll) )
        print(c.fetchone())
    
    elif choice==4:
        ed_roll=int(input("Enter Roll number: "))
        print("""What you want to update...
        Select 1 for Name
        Select 2 for Email Id
        Select 3 for Gender
        Select 4 for Phone Number
        Select 5 for Branch""")
        updateChoice=int(input("Enter your Choice: "))
        if updateChoice==1:
            updatedName=input("Enter New Name: ")
            c.execute("UPDATE student_info SET name=? WHERE roll=?",(updatedName,ed_roll))
            print("Name updated succesfully!!!")
        elif updateChoice==2:
            updatedemail=input("Enter New email id: ")
            c.execute("UPDATE student_info SET email=? WHERE roll=?",(updatedemail,ed_roll))
            print("Email updated Sucessfully!!!")
        elif updateChoice==3:
            updatedgender=input("Enter Your Gender: ")
            c.execute("UPDATE student_info SET gender=? WHERE roll=?",(updatedgender,ed_roll))
            print("Gender Updated Sucessfully!!!")
        elif updateChoice==4:
            updatedphone=input("Enter New Phone Number: ")
            c.execute("UPDATE student_info SET phone=? WHERE roll=?",(updatedphone,ed_roll))
            print("Phone Number Updated Sucessfully!!!")
        elif updateChoice==5:
            updatedbranch=input("Enter New Branch: ")
            c.execute("UPDATE student_info SET branch=? WHERE roll=?",(updatedbranch,ed_roll))
            print("Branch Updated Sucessfully!!!")
        else:
            exit
    elif choice ==5:
        dlroll=int(input("Enter roll number to delete data: "))
        c.execute("DELETE from student_info WHERE roll={}".format(dlroll))
        print("Data deleted succesfully!!!")
    
    else:
        break
