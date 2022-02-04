def menu():
    print("*"*70)
    print("""                 Menu
                         1.Add
                         2.Update
                         3.DisplayAllDetails
                         4.Display perticular student Details
                         5.Delete 
        """)
   
stud={11:{'Rollno':11,'Fname':'Shekhar','Lname':'Patil','Class':"Tybsc",'faculty':"Computer"}}
def add():
    name={}
    roll_no=eval(input("Enter the student Roll NNumber"))
    f_name=input("Enter the  First name")
    l_name=input("Enter the Last name")
    s_class=input("Enter the class of student")
    s_faculty=input("Enter the Faculty")
    name['RollNo']=roll_no
    name['Fname']=f_name.capitalize()
    name['Lname']=l_name.capitalize()
    name['Class']=s_class.capitalize()
    name['Faculty']=s_faculty.capitalize()
    stud[roll_no]=name

def update():
    
    while True:
        roll_no=eval(input("Enter the studen Roll No"))
        print("*"*70)
        print("""You can update student 
                            Update_Menu
                            1.First_Name 
                            2.Last_Name
                            3.Faculty
        """)
        ch=eval(input("Enter your choice"))
        if ch==1:
            stud[roll_no]['Fname']=input("Enter sudent name").capitalize()
        
        elif ch==2:
            stud[roll_no]['Lname']=input("Enter the last name").capitalize()
        elif ch==3:
            stud[roll_no]['Faculty']=input("Enter the Faculty").capitalize()
        else:
            print("Plese Enter Valid Option from given in Update Menu ") 
        print(f"Roll_no:=>{roll_no} Record is updated succesfully")
        op=input("Do you wanr to con tinue y/n") 
        if op!='y':
            break      

def display():
    for i in stud:
        print(stud[i])
    pass
def per_display():
    roll_no=eval(input("Enter student roll no:=>"))
    for key ,value in stud.items():
        if key==roll_no:
            print(value)

def delete():
    roll_no=eval(input("Enter the Student Roll no:=> "))
    del stud[roll_no]
    print(f"Roll No {roll_no} is deleted")
while True:
    menu()
    opt=eval(input("Enter the any one option"))
    if opt==1:
        add()
    elif opt==2:
        update()
    elif opt==3:
        display()
    elif opt==4:
        per_display()
        
    elif opt==5:
        delete()
    else:
        print("Enter valid Option ") 
    print("Do you want to continue  ???") 
    ch=input("Enter y for yes or n for no :=> ")
    ch=ch.upper()
    if ch!='Y':
        break


