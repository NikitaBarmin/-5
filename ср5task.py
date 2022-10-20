n = input('Введите число' )
n1 = float(n)
n2 = int(n1)
if n1 != n2:
    print('Ошибка. Число не может быть дробным')
elif int(n) <= 0:
    print('Ошибка. Число должно быть > 0')
else:
    sistem = int(input('Введите систему счисления(2 либо 8) '))
    if sistem == 2:
        n = int(n)
        c = ''
        while n > 0:
            c = str(n % 2) + c
            n //= 2
        print(c)
    elif sistem == 8:
        n = int(n)
        d = ''
        while n > 0:
            d = str(n % 2) + d
            n //= 2
        print(d)
    else:
        print('Ошибка. Вы ввели неправильную систему счисления')