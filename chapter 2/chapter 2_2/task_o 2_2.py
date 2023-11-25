number1 = input()
number2 = input()
d1 = int(number1[0])
d2 = int(number1[1])
d3 = int(number2[0])
d4 = int(number2[1])
sum_all_digits = d1 + d2 + d3 + d4
max_d = max(d1, d2, d3, d4)
min_d = min(d1, d2, d3, d4)
sum_min_and_max = max_d + min_d
sum_last_digits = (sum_all_digits - sum_min_and_max) % 10
print(f'{max_d}{sum_last_digits}{min_d}')
