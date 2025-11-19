a=float(input("Enter first number: "))
b=float(input("Enter second number: "))

#Declare functions
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
      return "Error"
    return a/b  
  
#Declare operations
print("Simple Calculator")
print("Operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

#Take input from the user
choice=input("Select operation (1/2/3/4) or 'q' to quit:")

if choice=='q':
        print("Calculator is closed")
    
if choice=='1':
        result=add(a,b)
        print("Result: ",result)
elif choice=='2':
        result=sub(a,b)
        print("Result: ",result)
elif choice=='3':
        result=mul(a,b)
        print("Result: ",result) 
elif choice=='4':
        result=div(a,b)
        print("Result: ",result)  
else:
        print("Error")