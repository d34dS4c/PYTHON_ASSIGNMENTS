a=input("enter string")
b=int(len(a))
first=str(a[:b])
second= str(a[b:])
if(first==second):
    print('string is symmetric')
elif(a==a[::-1]):
    print('string is palingdrome')
else: print('string is neither palingdrome nor symmetric')
