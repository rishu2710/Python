print("Enter two no. to perform any simple calculator")
a = int(input("Enter no. 1 : "))
b = int(input("Enter no. 2 : "))
print("Enter 1 for Addition (+) \nEnter 2 for Subtraction (-) \nEnter 3 for Division (/) \nEnter 4 for Multiplication (*) \n Enter 5 for exit.")
operation = input("Provide required input : ")
if operation == '1':
    print("Addition of both the value is : ",a+b)
elif operation == '2':
    print("Subtraction of both the value is : ",a-b)
elif operation == '3':
    print("Division of both the value is : ",a/b)
elif operation == '4':
    print("Mutiplication of both the value is : ",a*b)
else:
    print("Not a proper operation selected...... Programming Exiting...........")