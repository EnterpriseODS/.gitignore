a = (input("enter the first number "))
b = (input("enter the second number "))
# validation and data type assignment
try:
    a = int(a)
except ValueError:
    a = float(a)
try:
    b = int(b)
except ValueError:
    b = float(b)

operation = input("choice operations: (* ; / ; - ; + ) ")

result = 0

if operation == '+':
    result = (a + b)
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b
elif not operation in ['*' or '/' or '-' or '+']:
    print('not a correct sign')
print(f'result: {result}')
