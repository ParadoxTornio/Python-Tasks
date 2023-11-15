a = int(input())
b = int(input())
c = int(input())
a_minus_b = 0
if a >= b:
    a_minus_b = a - b
else:
    a_minus_b = b - a
a_minus_b /= c
a_minus_b = round(a_minus_b, 2)
print("{:.2f}".format(a_minus_b))
