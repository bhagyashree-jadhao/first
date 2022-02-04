num1=int(input("Emnter the first number"))
num2=int(input("Enter the second number"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Floor Dividion \n6.Module")
ch=int(input("Enter your choice"))
if ch==1:
    print(f"Addition oif {num1} and {num2} = ",num1+num2)
elif ch==2:
    print(f"Subtraction of {num1} and {num2}",num1-num2)
elif ch==3:
    print(f"Multiplication of {num1} and {num2}=" ,num1*num2)
elif ch==4:
    print(f"Division of {num1} and {num2}=" ,num1/num2)

elif ch==5:
    print(f"floor division of {num1} and {num2}=" ,num1//num2)

elif ch==6:
    print(f"Reminder  of {num1} and {num2}=" ,num1%num2)

else:
    print("You Have enter Invalid Choice!!!")


