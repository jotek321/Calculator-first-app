while True:
    print('To jest kalkulator\nUżycie liczby zcrashuje calculatorn\n\n')
    num1 = float(input('liczba x równa się: \n'))
    num2 = float(input('liczba y równa się: \n'))
    fun = int(input('funkcje \n'
                    '1 to dodawanie,\n'
                    '2 to odejmowanie,\n'
                    '3 to mnożenie,\n'
                    '4 to dzielenie\n'))

    if fun == 1:
        print(num1 + num2)
    elif fun == 2:
        print(num1 - num2)
    elif fun == 3:
        print(num1 * num2)
    elif fun == 4:
        print(num1 / num2)
    else:
        print('ERROR')
