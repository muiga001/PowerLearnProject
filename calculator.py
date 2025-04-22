print("Hey there, welcome to this simple calculator...")

print("1 .Add\n2 .Subtract\n3 .Divide\n4. Multiply\n")

operation = int(input("Choose an operation : 1, 2, 3 or 4? "))

num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))

result = ""

if operation == 1:
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")    
elif operation == 2:
    result = num1 - num2
    print(f"{num1} - {num2} = {result}") 
elif operation == 3:
    result = num1 / num2
    print(f"{num1} / {num2} = {result}") 
elif operation == 4:
    result = num1 * num2
    print(f"{num1} * {num2} = {result}") 