def calculator():
    operation = input("please select an operation (+,-,*,/):")
    num1 = float(input("enter the first number:"))
    num2 = float(input("enter the second number:"))
if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2) 
elif operation == '*':
    print(num1 * num2)  
elif operation == '/':
    print(num1 / num2)
else:
    print("Invalid operation") 

calculator()                    