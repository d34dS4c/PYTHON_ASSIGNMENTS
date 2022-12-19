a=input('enter string: ')
b=a.split(' ')
for i in range(len(b)):
    if(len(b[i])%2==0):
        print(b[i])

