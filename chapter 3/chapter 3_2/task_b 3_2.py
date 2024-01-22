n = input()
n2 = input()
set_n = set(n)
set_n2 = set(n2)

for i in set_n & set_n2:
    print(i, end='')
