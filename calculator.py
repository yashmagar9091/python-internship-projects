print("welcome to the codsoft calculator")
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("Choose the operations you want to perform:")
operator=input("enter the operator:'+' , '-' ,'*' ,'/' ,'%'  :")
if(operator=="+"):
    print("Addition=",num1+num2)
elif(operator=="-"):
    print("Subtraction=",num1-num2)
elif(operator=="*"):
    print("Multiplication=",num1*num2)
elif(operator=="%"):
    print("Remainder=",num1%num2)

if(num2==0):
    print("Division is not possible here")
else:
    print("Division=",num1/num2)

