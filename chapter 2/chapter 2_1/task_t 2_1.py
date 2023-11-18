n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
x2 = (n * m - k1 * n) // (k2 - k1)
x1 = n - x2
print(f'{x1} {x2}')
