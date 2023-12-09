n = input()
max_digit = int(n[0])
for i in n:
    if int(i) > max_digit:
        max_digit = int(i)

print(max_digit)
