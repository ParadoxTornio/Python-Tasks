n = int(input())
m = int(input())
a = 7
b = 6
a -= 3
b += 3
a += 2
b += 5
b -= 2
a += n
b += m
if a >= b:
    print('Петя')
else:
    print('Вася')
