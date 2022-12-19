'''Пользователь вводит с клавиатуры три числа в переменные a, b, c.
Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no'''

a, b, c = int(input('number a: ')), int(input('number b: ')), int(input('number c: '))
if (a + b + c) > 10 and (a + b) % 3 == 0:
    print('yes')
else:
    print('no')
