'''str1=input("Enter any string")
vowels=['a','e','i','o','u']
i=0
count=0
while i<len(str1):
    if str1[i] in vowels:
        print(str1[i])
        count+=1
    i+=1
print(count)'''
'''num=int(input("Enter the number"))

i=0
while i<=20:
    print(i)
    i+=num
'''
no=int(input("How many table u want to display"))
j=1
while j<=no:
    num=int(input("Enter the number"))
    i=1
    while i<=10:
        print(f"{num} *{i} =", num*i)
        i+=1
    j+=1

  