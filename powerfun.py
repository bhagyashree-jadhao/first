'''def my_power(num):
    print(num*num)
my_power(5)'''
#from itertools import count


'''d=0
def my_power(n):
    d=n*n
    print(d) 
my_power(n=7)

def my_len(s):
    count=0
    for i in s:
        count+=1
    print(count)
my_len("Python")     
'''
def my_len(*args):
    c=0
    for i in args:
        c+=1
    print(c)
    print(type(args))
    print(args)
my_len('ram',"Python",4,True)

def mylength(**kwargs):
    print(f" The name is {kwargs['name']} and his age is {kwargs['age']}")
mylength(name='ram',age=6)
mylength(name="Rohan",age=8)
def email_id(**kwar):
    email=kwar['fname']+str(kwar['eid'])+"@python.com"
    print(f"email _id of {kwar['fname']} is {email }")
    print(kwar['eid'])
email_id(fname='rohan',eid=456)
email_id(fname='raj',eid=111)

 


