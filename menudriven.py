while True:
    
    print("What you want to do \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

    number=int(input("Enter any one obtion"))
    num1=int(input("Enter the first number="))
    num2=int(input("Enter the second number="))
    if number==1:
        print("Addition of {num1} + {num2}=",num1+num2)
    elif number==2:
        print(f"{num1} - {num2}",num1-num2)
    elif number==3:
        print(f"{num1} * {num2}",num1*num2)
    elif number==4:
        print(f"{num1} / {num2}",num1/num2)
    else:
        print("Invaid Option")
    ans=input("do you want to continue(y/n)?:")
    if ans=='n':
        break
    