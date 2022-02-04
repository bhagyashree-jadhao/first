'''a=0
b=1
n=int(input("Enter the range"))
print(f"Fibbonacci series of {n} terms : ")
i=1
while i<=n:

    
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i+=1'''
n=5
for i in range (5):
    for j in range(i+1):
        print(i,end=" ")
        #print('*',end=" ")
        
    print()
''' 
0 
1 1 
2 2 2
3 3 3 3
4 4 4 4 4

'''  

n=5
for i in range (5):
    for j in range(1,i+1):
        print(i,end=" ")
        #print('*',end=" ")
        
    print()    

'''   
1
2 2
3 3 3
4 4 4 4'''
n=5
for i in range(5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
1
1 2
1 2 3
1 2 3 4
'''
n=5
for i in range (1,11):
    for j in range(i+1,i+2):
        print(n*j,end=" ")
        
    print()