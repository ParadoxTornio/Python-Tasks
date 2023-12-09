a = int(input())
b = int(input())
c = int(input())

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a

if a ** 2 == b ** 2 + c ** 2:
    print('100%')

elif a ** 2 < b ** 2 + c ** 2:
    print('крайне мала')

else:
    print('велика')
