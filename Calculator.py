print('')
print('')
print('')
print('Welcome to Xhicko Logical Calculator')
print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
print('')

def operation_logic():

    num1 = int(input('Enter First Number: '))
    num2 = int(input('Enter Second Number: '))
    operator = input('Enter Operator (Add, Sub, Div, Mul & Mod): ')

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



def re_run():
    while True:
        print('')
        re_run = input('Do you want to make another calcultion? (Yes or No) : ')
        print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
        if re_run == 'No':
            print('')
            print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
            print('You have successfully Ended the Calculation Programme')
            print('Byee')
            print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _  ')
            print('')
            break
        operation_logic()

re_run()