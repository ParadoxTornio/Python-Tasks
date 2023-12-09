import math


n = int(input())

if n <= 1:
    print('NO')

else:
    simple = True
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            simple = False
            break
    if simple:
        print('YES')
    else:
        print('NO')
