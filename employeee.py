import email
from unicodedata import name
def menu():
    print('*'*70)
    print("         Welcome to Employee Managament System      " )
    print("_______________________________________________________________________")
    print("""                            Menu
                    1.Add Employee Details
                    2.Update Employee Details
                    3.Delete Employee Details
                    4.Display All Details
                    """)
    print('*'*70)
db={'shekhar':{'Name':"Shekhar",'Id':101,'salary':45000,'Email':"shekhar101@acs.com",'dept':"IT",'age':34,}}

def add_emp():
    db2={}
    emp_name=input("Enter the employee Name: ")
    emp_id=eval (input("Enter the employee Id : "))
    emp_salary=eval(input("Enter the employee salary : "))
    emp_age=eval(input("Enter the employee age : "))
    emp_email=emp_name.lower()+str(emp_id)+'@acs.com'
    emp_dept=input("Enter the Department ")
    db2['Name']=emp_name.capitalize()
    db2['Id']=emp_id
    db2['salary']=emp_salary
    db2['dept']=emp_dept
    db2['age']=emp_age
    db2['Email']=emp_email

    db[emp_name]=db2
    print(f"Employee {emp_name} is added successfully")
    print(db)
def update():
    print("*"*50)
    print("""        Update the Employee Details
                    1.Salary
                    2.age
                    3.Depatment                
                                    
                    """)
    opt=eval(input("Enter the any one option:=> "))
    emp_name=input("Enter the name of Employee:=> ")
    if opt==1:
         db[emp_name]['salary']=eval(input("Enter the new Salary"))
         print(f"Empployee {emp_name} salary is updated successfully!!!")
       
    elif opt==2:
        db[emp_name]['age']=eval(input("Enter the age"))
        print(f"Empployee {emp_name} age is updated successfully!!!")
       
        
    elif opt==3:
        db[emp_name]['dept']=input("Enter the Department")
        print(f"Empployee {emp_name} department is updated successfully!!!")
    else:
        print("Please Enter the Valid Option")   
        
    print("*"*50)

def delete_emp():
    emp_name=input("Enter the employee name")
    del db[emp_name]
    print(f"Employee {emp_name} is delete successfully!!!")

def display():
    for i in db:
        print(db[i])
        print(f"Name--->{db[i]['Name'] } Id--->{db[i]['Id'] } Age--->{db[i]['age']} Email--->{db[i]['Email']} Salary--->{db[i]['salary']}")
    pass
while True:
    menu()
    
    ch=eval(input("Enter your choice"))
    
    if ch==1:
         add_emp()
    elif ch==2:
        update()
    elif ch==3:
        delete_emp()
    elif ch==4:
        display()
    else:
        print("You Enter Invalid Option")
    n=input("Do you eant to continue! y/n")
    n=n.lower()
    if n!='y':
         break