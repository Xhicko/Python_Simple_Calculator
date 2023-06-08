print('Welcome to xhicko Logical Calculator')
print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')

num1 = int(input('Enter First Number: '))
num2 = int(input('Enter Second Number: '))
operator = input('Enter Operator (Add, Sub, Div, Mul & Mod): ')


def operation_logic():
    if operator == 'Add' :
       result = num1 + num2
       print(f'Your Added Result Is... {result}')

    elif operator == 'Sub':
        result = num1 - num2
        print(f'Your Subracted Result is... {result}')
        
    elif operator == 'Div':
        result = num1 / num2
        print(f'Your Divided Result is... {result}')

    elif operator == 'Mul':
        result = num1 * num2
        print(f'Your Multiplied Result is... {result}')

    elif operator == 'Mod':
        result = num1 % num2
        print(f'Your Modulated Result is... {result}')
    else:
        print('Not A Valid Operator')
    
operation_logic()

