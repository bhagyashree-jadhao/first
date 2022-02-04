'''n=int(input("Enter the number"))
m=str(n)
p=m+m
#print(m)
#print(p)
k=m*3
#print(k)
add=n+int(p)+int(k)
print(f"{n} + {p} + {k}={add}")'''
#Given two integer numbers return their product only if the product is greater than 1000, else return their sum.
'''num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
if (num1*num2>=1000):
    print(num1+num2)
else:
    print(num1*num2)'''
#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number
'''i=0
pre_num=0
sum=0
while True:
    if i<10:
        
        sum=pre_num+i
    
        pre_num=i
        i+=1

        print("Current Number", i, "Previous Number ", pre_num, " Sum: ", sum)
    else:
        break'''
#Write a program to accept a string from the user and display characters that are present at an even index number.
'''str1=input("Enter the string")
str2=" "
i=0
while i < len(str1):
    if i%2==0:
        #print(i)
        print("even index characater in given string are:",str1[i])
    i+=1'''
'''num=int(input(" Enter the number"))
i=1
sum=0
while i <=num:
    sum+=i
    i+=1
print(sum)'''
#Write a program to count the total number of digits in a number using a while loop.
'''num=int(input("Enter the number"))
count=0
while num!=0:
    num=num//10
    count+=1
print(count)'''
#Iterate the given list of numbers and print only those numbers which are divisible by 5
'''list1=[10,20,30,40,55,65,76,89,75,80]
i=0
#for  i in list1:
while i <len(list1):
    if list1[i]%5==0:
        print(f"{list1[i]} no are divisble 5")
    i+=1

'''
'''str_x = "Emma is good developer. Emma is a writer"
i=0
count=1
while i <len(str_x):
    if str_x[i]=="Emma":
        
        count+=1
    else: 
        continue

    i+=1
print(count)'''
'''sum=0
sum1=0
i=0
while i<=10:
    if i%2==0:
        sum+=i
    
    else:
        sum1+=i

    i+=1
print("sum of all even no is :-",sum)
print("sum of all odd no is:->", sum1)'''
# Print number in reverse number
'''num=2345
d=0
while num!=0:
    m=num%10
    d=(d*10)+m
    num=num//10
print(d)'''


# Print list element using a loop

'''list1 = [10, 20, 30, 40, 50]
i=0
while i < len(list1):
    print(list1[i])
    i+=1'''

#Print list element in reverse using a loop

'''list1 = [10, 20, 30, 40, 50]
i=len(list1)-1
while i >= 0:
    print(list1[i])
    i-=1'''
#Check Palindrome Number
#Write a program to check if the given number is a palindrome number.
'''num=int(input('Enter the number'))
i=0
k=0
num1=num
while num !=0:
    n=num%10
    k=(k*10)+n
    num=num//10
    
if num1==k:
        print(f"{k} is palindrom number   ")
else:
        print(f"{k} is not palindrom")
'''
#Print multiplication table form 1 to 10
'''i=1
n=int(input("Enter the number"))
while i<=10:

        print(i*n)
        i+=1'''

'''i = int(input(" Please Enter any Positive Integer lessthan 10 : "))

print(" Multiplication Table ")

while(i <= 10):
    j = 1
    while(j <= 10):
        print('{0}  *  {1}  =  {2}'.format(i, j, i*j))
        j = j + 1
    print('==============')
    i = i + 1'''
'''i=1

while i<=10:
    j=1
    while j<=10:
        print(i*j,end=" ")
        j+=1
    print()
    i+=1'''
'''x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)'''

'''x = 0
while (x < 100):
  x+=2
print(x)'''

x=1
y=1
while x<6:
    while y <x:
        print(x)
    x+=1

    


