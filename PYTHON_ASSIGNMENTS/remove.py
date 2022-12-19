

string=input('enter string: ')
i=int(input('enter i :'))
print('1,merge string \n 2.string replace')
n=int(input('enter the type no :'))
if(n==1):
    #merge string
    a = string[ : i]
    b = string[i + 1: ]
    print(''+a+b)
elif(n==2):
    #string replace
    for j in range(len(string)):
        if j == i:
            string = string.replace(string[i], "", 1)
    print(string)
else: print('invalid selection')
