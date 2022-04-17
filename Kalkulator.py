def calculator():
    try: 
        print('Using a letter will resolt in crash\n')
        num1 = float(input('x is equal to: \n'))
        num2 = float(input('y is equal to: \n'))
        fun =  (input('functions \n'
                        '1 is addition,\n'
                        '2 is subtraction,\n'
                        '3 is multiplication,\n'
                        '4 is division.\n'))

        if fun == '1':
            print(num1 + num2)
        elif fun == '2':
            print(num1 - num2)
        elif fun == '3':
            print(num1 * num2)
        elif fun == '4':
            print(num1 / num2)
        else:
            print('error')

    except ZeroDivisionError as exeption_name:
        print(exeption_name)
        print("You can't divide by 0.")
    except ValueError as exeption_name:
        print(exeption_name)
        print('Enter only numbers.')
    except Exception as exeption_name:
        print(exeption_name)
        print('Some thing went wrong.')

while True:
    print('It is multipurpose tool')
    option = input('To open: \n calculator enter 1 \n')

    if option == '1':
        calculator()
    elif option > '1':
        print('error wrong number')
    elif option < '1':
        print('error wrong number')
    else:
         pass

