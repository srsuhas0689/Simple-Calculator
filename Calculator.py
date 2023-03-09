operation=input(str("Select an operation\n{ '+' , '-' , '*' , '/' , '**' , '%' , 'sqrt'}"))
num1=int(input("Enter a number "))
num2=int(input("Enter a number "))
Add=num1+num2
Sub=num1-num2
Mul=num1*num2
Div=num1/num2
Mod=num1%num2
Pow=num1**num2
sqrt=num1=num2**0.5
if operation=='+':
    print(Add)
elif operation=='-':
    print(Sub)
elif operation=='*':
    print(Mul)
elif operation=='%':
    print(Mod)
elif operation=='**':
    print(Pow)
elif operation=='sqrt':
    print(sqrt)
else:
    print(Div)