n = input()
new_str_n = ''

for i in n:
    if int(i) % 2 != 0:
        new_str_n += i

print(new_str_n)
