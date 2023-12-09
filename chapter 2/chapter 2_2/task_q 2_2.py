import math


a = float(input())
b = float(input())
c = float(input())

if a == 0 and b == 0 and c == 0:
    print('Infinite solutions')
elif a == 0 and b == 0 and c != 0:
    print('No solution')
elif a == 0 and b != 0:
    print(-c / b)
else:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('No solution')
    elif d == 0:
        print(-b / (2 * a))
    else:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print(min(x1, x2), max(x1, x2))
