#making a simple calculator
a= int(input('enter a number'))
b= int(input('enter a number:'))
c= input('enter the operation to be done +,-,*,/')
if c == '+':
    print(a+b)
elif c =='-':
    print(a-b)
elif c =='*':
    print(a*b)
elif c=='/':
    if b == 0:
        print('error: division by 0 is not possible')
    else:
        print(a/b)
else:
    print('invalid operation select from +-*/')
        
    


print()        
