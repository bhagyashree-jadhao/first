'''str_x = "Emma is good developer. Emma is a writer"
i=0
count=0
while i <len(str_x):
    if str_x[i:i+4] =="Emma":
        
        count+=1

    i+=1
print(count)'''
'''
count=0
for i in range(len(str_x)-1):
    if str_x[i:i+4]=='Emma':
        count+=1
print(count)'''
'''i=1
while i <= 5:
    j=1
    while j<=i:
        print(i,end=" ")
        j+=1
    #new line after each row
    print('')
    i+=1'''
i=1
while i<=5:
    j=i
    while j<=i:
        print(i,end=' ')
        j+=1
    print('')
    i+=1

s="shekhar"
print(s[-7:-3])
print(s[: :-1])

