def add(num1,num2):
    print(f"Addition of {num1} + {num2}=",num1+num2)
def sub(num1,num2):
    print(f"Subtraction  of {num1} + {num2}=",num1-num2)
def mult(num1,num2):
   print(f"Multiplication of {num1} + {num2}=",num1*num2)
def div(num1,num2):
       print(f"Division of {num1} + {num2}=",num1//num2)
def display():
    print('*'*10,"Welcome to Calculator",'*'*10)
    def star():
        print('*'*50)
    while True:
        star()

        print("What you want to do \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
        star()
        choice=int(input("Enter any one obtion"))
        num1=eval(input("Enter the first Number"))
        num2=eval(input("Enter the second number"))
        
        if choice==1:
            add(num1,num2)
        elif choice==2:
            pass
        elif choice==3:
            sub(num1,num2)
        elif choice==4:
            div(num1,num2)
        else:
            print("Invalid Option")
        star()
        n=input("Do you want to continue!!! y/n")
        if n=='n':
            break
display()   


