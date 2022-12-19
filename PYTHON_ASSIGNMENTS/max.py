def max(a,b,c):
    if(a>b):
        if(a>c):
            print('a is greater')
    if(b>c):
        if(b>a):
            print('b is greater')
    if(c>a):
        if(c>b):
            print('c is greater')
a=int(input('enter no '))
b=int(input('enter no '))
c=int(input('enter no '))
max(a,b,c)
