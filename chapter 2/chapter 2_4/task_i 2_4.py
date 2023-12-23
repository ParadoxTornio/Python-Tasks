n = int(input())
big_number = ''

for i in range(n):
    numbers = input()
    max_digit = numbers[0]
    for digit in numbers:
        if digit > max_digit:
            max_digit = digit
    big_number += max_digit

print(big_number)
