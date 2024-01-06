numbers = input()
list_of_numbers = numbers.split()
a = int(list_of_numbers[0])

for i in range(1, len(list_of_numbers)):
    b = int(list_of_numbers[i])
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a

    a = max(a, b)

print(a)
