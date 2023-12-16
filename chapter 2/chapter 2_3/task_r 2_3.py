n = int(input())
divisor = 2
multipliers = ''

while n != 1:
    if n % divisor == 0:
        n /= divisor
        multipliers += str(divisor)
        if n != 1:
            multipliers += ' * '
    else:
        divisor += 1

print(multipliers)
