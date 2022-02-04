def menu():
    print('*'*70)
    print("""      ======== Welcome to Employee Managment system =======
                               MENU
                                
                             1. ADD
                             2. Update
                             3. Display
                             4. Delete
                             5. Display Perticular data

                            """)
    print('*'*70)
emp_list=[[11,"Rohan"," Kadam","rohankadam@acs.com",'IT',50000]]
def add():
    list1=[]
    e_id=eval(input("Ente employee id = "))
    list1.append(e_id)
    name=input("Enter employee name = ").capitalize()
    list1.append(name)
    l_name=input("Enter employee name").capitalize()
    list1.append(l_name)
    Email=name+l_name+'@acs.com'
    Email=Email.lower()
    list1.append(Email)    
    e_dept=input("Enter department name").capitalize()
    list1.append(e_dept)
    
    salary=eval(input(f"Enter the Employee {name} Salary:=> "))
    list1.append(salary) 
    emp_list.append(list1)
    print(f"Record of   {name}  is inserted successfully....... ")
def update():
    name=input("Enter the name of employee")
    for i in range(len(emp_list)):
        
        for j in range(len(emp_list[i])):
    
            if name == emp_list[i][j]:
                print(f" we can update {name} record")
            
   
    print("""  Update Menu
                
                1. Name
                2. Department
                3. salary""")
    op=eval(input("Enter your choice  :=> "))
    if op==1:
         emp_list[i][1]=input("Enter the employee name :=> ").capitalize()
         emp_list[i][2]=input("Enter the last name").capitalize()
    elif op==2:

        emp_list[i][4]=input("Enter Deprtment name of => ").capitalize()
    elif op==3:
        emp_list[i][5]=input("Enter the Salary = ")
    
    else:
        print( "You have Entered Invalid Option "  )
    
    print(f" Employee {emp_list[i][1]} is updated successfully....... ")
def display():
    print("Employee Record are : ")
    for i in emp_list:
        print(i,)
def delete():
    name=input("enter the name of employee= ").capitalize()
    for i in range (len(emp_list)):
        
        for j in range(len(emp_list[i])):
    
            if name == emp_list[i][j]:
                print(f"{name}'s record will be deleted..........")
                
              

    
    del emp_list[i]
    print(f"Record of {name}   is deleted successfully....")


def dis_per_data():

    name=input("enter the name of employee= ").capitalize()
    for i in range (len(emp_list)):
        
        for j in range(len(emp_list[i])):
    
            if name == emp_list[i][j]:
                print("Record found in list no :", i+1)
            
                print(f"Employee {emp_list[i][1]} Record is := {emp_list[i]} ")
            
while True:
    menu()
    op=eval(input("Enter your choice => "))
    if op==1:
         add()
    elif op==2:
        update()
    elif op==3:
        display()
    elif op==4:
        delete()
    elif op==5:
        dis_per_data()
    else:
        print(" You Entered Invalid Option")
    ch=(input("Do you want to continue y/n .....   ")).upper()
    if ch!='Y':
        break

                        





















