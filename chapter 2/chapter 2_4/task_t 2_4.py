n = int(input())
max_summa = 0
answer = 0

for base in range(2, 11):
    summa = 0
    num = n
    while num != 0:
        summa += num % base
        num //= base
    if summa > max_summa:
        max_summa = summa
        answer = base

print(answer)
