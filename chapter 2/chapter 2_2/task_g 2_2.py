n = input()
n2 = n.replace(' ', '')
rev_n2 = n2[::-1]
print(rev_n2)
if rev_n2 == n2:
    print('YES')
else:
    print('NO')
