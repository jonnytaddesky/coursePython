def printMax(x, y):
    '''Выводит максимальное из двух чисел.

    Оба значения должны быть целыми числами.'''
    x = int(x)  # Конвертируем в целые, если возможно
    y = int(y)

    if x > y:
        print(x, 'maximum')
    else:
        print(y, 'maximum')


help(printMax)
printMax(3, 5)
print(printMax.__doc__)
