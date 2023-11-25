number = input()
digit_1 = number[0]
digit_2 = number[1]
digit_3 = number[2]
min_number = None
max_number = None
max_d = int(max(digit_1, digit_2, digit_3))
min_d = int(min(digit_1, digit_2, digit_3))
sum_max_and_min = max_d + min_d
mid_d = (int(number[0]) + int(number[1]) + int(number[2])) - sum_max_and_min
if min_d != 0:
    min_number = int(str(min_d) + str(mid_d))
elif mid_d != 0:
    min_number = int(str(mid_d) + str(min_d))
else:
    min_number = int(str(max_d) + str(min_d))

max_number = int(str(max_d) + str(mid_d))
print(f'{min_number} {max_number}')
