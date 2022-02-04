#Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
#using while loop
'''list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3=[]
list4=[]
i=0
while i<len(list1):
    if list1[i] %2!=0:
        #print(list1[i])
        list3.append(list1[i])
    i+=1
i=0
while i<len(list2):
    if list2[i]%2==0:
        list3.append(list2[i])
    i+=1

print(list3)'''
#forloop
'''list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3=[]
for num in list1:
    if num %2!=0:
        list3.append(num)

for num in list2:
    if num %2==0:
        list3.append(num)
print(list3)'''
'''l=[10,'a',True,45.7]
l[1]=6
print(l)
l.append("ram")
print(l)
print(l[1:4])
l.remove(True)
print(l)
del l[3]
print(l)'''
#l=[]
#n=eval(input("Enter the number "))
i=1
'''while i <=n:
    if i==1:
        k=eval(input(f"Enter the {i}st Element in list"))
    elif i==2:
        k=eval(input(f"Enter the {i}nd Element in list"))
    else:
   
        k=eval(input(f"Enter the {i}th Element in list"))
    l.append(k)
    i+=1
print(" List is :->",l)

# how many numbers are present in the list.
#l=[12,23,45,'ram','neha',5]
count=0
#
for i in l:
    if isinstance(i,int):
        count+=1 
        
print(count)'''

 


'''s="ram6574"
#print(s.isalnum())
for i in s:
    if i.isdecimal():
        print(i)
'''
# list of numbers and a string
'''ls = [1, 2, 3, 4, 'cat']
# check if list contains only numbers
count=0
print(all([isinstance(item, int) for item in ls]))
for i in l:
    if isinstance(i,int):
        count+=1
print(count)

'''
# Reverse a list in Python
#list1 = [1, 2, 3, 4,6]
'''print(list1[::-1])
for i in list1:
    list1.append(i)'''

#Exercise 3: Turn every item of a list into its square
'''list2=[]
for i in list1:
    list2.append(i*i)
   
print(list2)'''
# Print largest and smallest number in list
#list1 = [10, 2, 30, 40,60]    
#max1=list1[0]
                                                                                                         
#for i in list1:
#  if i>max1:
#       max1=i
'''i=0  
l2=[]      
while i <len(list1):
    if list1[i]>max1:
        max1=list1[i]
        l2.append(max1)
    i+=1
print(max1)
print(l2)'''
'''l2=[]
list1 = [10, 20, 30, 23,85,40,60]
list2=[]
#min1=list1[0]
while list1:
    min1=list1[0]
    for i in list1:
        if  i<min1:
            min1= i
    l2.append(min1)
    list1.remove(min1)
print(l2) '''  
'''my_list = [4, 2, 3, -1, -2, 0, 1]
new_list = []

while my_list:
    min = my_list[0]
    for x in my_list:
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)

    
print(new_list)
'''

'''def list_create():
    list1=[]
    n=eval(input("Enter the number"))
    i=1
    while i<=n:
        k=eval(input("Enter the element in list"))
        list1.append(k)
        i+=1
    #print(list1)
    def min1():
        min_no=list1[0]
        for i in list1:
            if i<min_no:
                min_no=i
        print(f"Minimum number in {list1} is {min_no}")
    min1()
    def max1():
        max_no=list1[0]
        i=1
        while i<len(list1):
            if max_no<list1[i]:
                max_no=list1[i]
            i+=1
        print(f"Maximum number in {list1} is {max_no}")
    max1()
    def as_sort():
        for i in range(0,n):
            for j in range(i+1,n):
                if list1[i]>list1[j]:
                    temp=list1[i]
                    list1[i]=list1[j]
                    list1[j]=temp
        print(f"ascending list => {list1}")
    as_sort()
list_create()'''
l=[[1,'ram','Tybsc0',55],[2,"neha",'Sybsc',77]]
#name=input("Enter the name")
'''for i in range (len(l)):
   
    if name in l:
        print(l[i])'''
li=[['a', 'b', 'new', 'mpilgrim', 'z'], ['example', 'new', 'two', 'elements']]
name=input("enter")
for i in range (len(li)):
    for j in range(len(li[i])):
    
        if name == li[i][j]:
            print("\nElement found at Position:", i+1,j+1)
            print(li[i])

    