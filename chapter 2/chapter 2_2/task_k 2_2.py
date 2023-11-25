number = input()
max_d = int(max(number))
min_d = int(min(number))
sum_max_and_min = max_d + min_d
last_d = (int(number[0]) + int(number[1]) + int(number[2])) - sum_max_and_min

if sum_max_and_min == last_d * 2:
    print('YES')
else:
    print('NO')
