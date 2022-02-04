import functools
from re import I


'''n=int(input("Enter the number"))
i=1
s=1

while i<=n:
    s=s*i
    i+=1
print(f"Factor of {n} is {s}")'''
'''l=[10,20,30]
s=functools.reduce(lambda a,b:a+b,l)
print(s)
l = [1,2,3,4]
			
def sum1(a,b):
		return a+b

total = functools.reduce(sum1, l) 
print(total)'''
l="python programming"
v=['a','e,','i','o','u']
s=(filter(lambda a: True if a in v else False,l))
print(list(s))
s1=tuple(map(lambda a : a*2,l))
print(s1)
l2=(20,30,40,50,60,70)
s2=tuple(map(lambda a: a+5,l2))
print(s2)
s3=list(filter(lambda a,b:True if a>b else False,l2) )

print(s3)
