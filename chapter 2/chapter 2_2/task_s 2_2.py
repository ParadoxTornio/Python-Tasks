x = float(input())
y = float(input())

if x ** 2 + y ** 2 > 10 ** 2:
    print('Вы вышли в море и рискуете быть съеденным акулой!')

elif x < -7:
    print('Зона безопасна. Продолжайте работу.')

elif x > 5:
    print('Зона безопасна. Продолжайте работу.')

elif x <= 5 and x >= 0 and y >= 0:
    if x ** 2 + y ** 2 <= 5 ** 2:
        print('Опасность! Покиньте зону как можно скорее!')
    else:
        print('Зона безопасна. Продолжайте работу.')

elif x >= -4 and x <= 0 and y >= 0:
    if y <= 5:
        print('Опасность! Покиньте зону как можно скорее!')
    else:
        print('Зона безопасна. Продолжайте работу.')

elif x >= -7 and x <= -4:
    if 5 / 3 * x + 35 / 3 >= y:
        print('Опасность! Покиньте зону как можно скорее!')
    else:
        print('Зона безопасна. Продолжайте работу.')
else:

    if 1 / 4 * x ** 2 + 1 / 2 * x - 35 / 4 <= y:
        print('Опасность! Покиньте зону как можно скорее!')
    else:
        print('Зона безопасна. Продолжайте работу.')
