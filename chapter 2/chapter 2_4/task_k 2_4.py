import math


n = int(input())
counter = 0

for i in range(n):
    num = int(input())
    simple = (num != 1)
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            simple = False
            break
    if simple:
        counter += 1

print(counter)
