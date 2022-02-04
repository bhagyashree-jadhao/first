'''d={1:45,2:"RAM",3:True,4:67}
for i in d.items():
    print(i)'''


'''d={'pavan':{'name':"Pavan",'age':34},'ramesh':{'name':"bavan",'age':44}}
print(d['pavan']['age'])
d['ramesh']['name']='JAY'
print(d)
for i in d.items():
    print(i)
d['neha']=input('Name')
print(d)'''
def my_emp():
    d={}
    n=eval(input("Enter the number"))
    i=0
    while i<=n:
        d['id']=input("Enter the id")
        d['name']=input("Enter the name") 
        i+=1
    for k in d.items():
        print(k)
my_emp()






