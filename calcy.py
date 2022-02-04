print("*****Welcome to calculator*****")
while 1:
    print('*'*50)
    print("What do you want to do \n1.  Addition\n2.  Subtraction\n3.  Multiplication\n4.  Division\n5.  Module")
    print('*'*50)
    number=eval(input("Enter any one obtion"))
    num1=int(input("Enter the first number="))
    num2=int(input("Enter the second number="))
    if number==1:
        print(f"Addition of {num1} and  {num2} =",num1+num2)
    elif number==2:
        print(f" Subtraction of {num1} and {num2} =",num1-num2)
    elif number==3:
        print(f" Multiplication of {num1} and  {num2} =",num1*num2)
    elif number==4:
        print(f" Division of {num1} and {num2} =",num1/num2)
    elif number==5:
        print(f" Reminder of {num1} and {num2} =",num1%num2)
    
    else:
        print("Invaid Option")
    ans=input("do you want to continue(y/n)?:")
    if ans=='n':
        break
    