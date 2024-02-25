def add(x,y):
    return x + y


def sub(x,y):
    return x - y


def mul(x,y):
    return x * y


def div(x,y):
    return x / y


def mod(x,y):
    return x % y


print('Select opration: ')
print('1. Add')
print('2. Sub')
print('3. Mul')
print('4. Div')
print('5. Mod')

choice = input('Enter the choices (1, 2, 3, 4, 5): ')

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

if choice == '1':
    print(f'Result of sum: {add(num1, num2)}')
elif choice == '2':
    print(f'Result of sub: {sub(num1, num2)}')
elif choice == '3':
    print(f'Result of mul: {mul(num1, num2)}')
elif choice == '4':
    print(f'Result of div: {div(num1, num2)}')
elif choice == '5':
    print(f'Result of mod: {mod(num1, num2)}')
else:
    print('Invalid input')