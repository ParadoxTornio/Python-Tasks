n = int(input())
counter = 0

for i in range(n):
    num = input()
    rev_num = num[::-1]
    if rev_num == num:
        counter += 1

print(counter)
