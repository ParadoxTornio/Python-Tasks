n = int(input())
max_summ = 0
name_of_winner = ''

for i in range(n):
    name = input()
    number = input()
    summ = 0
    for digit in number:
        summ += int(digit)
    if summ >= max_summ:
        max_summ = summ
        name_of_winner = name

print(name_of_winner)
