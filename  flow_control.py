# multifunctional calculator
a = float(input("enter the first number "))
operation = input("choice operations: (* ; / ; - ; + )")
b = float(input("enter the second number "))
result = 0

if operation == '+':
    result = (a + b)
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b
elif not operation in [ '*' or '/' or '-' or '+']:
    print('not a correct sign')

print(f'result: {result}')