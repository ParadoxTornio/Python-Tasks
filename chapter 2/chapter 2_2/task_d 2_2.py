n1 = int(input())
n2 = int(input())
n3 = int(input())
first_place = None
second_place = None
third_place = None

if n1 >= n2 and n1 >= n3:
    first_place = 'Петя'
elif n2 >= n1 and n2 >= n3:
    first_place = 'Вася'
else:
    first_place = 'Толя'

if n1 >= n2 and n1 < n3 or n1 >= n3 and n1 < n2:
    second_place = 'Петя'
elif n2 >= n1 and n2 < n3 or n2 >= n3 and n2 < n1:
    second_place = 'Вася'
else:
    second_place = 'Толя'

if first_place == 'Петя' and second_place == 'Вася' or\
        first_place == 'Вася' and second_place == 'Петя':
    third_place = 'Толя'
elif first_place == 'Петя' and second_place == 'Толя' or\
        first_place == 'Толя' and second_place == 'Петя':
    third_place = 'Вася'
else:
    third_place = 'Петя'

print(f'1. {first_place}')
print(f'2. {second_place}')
print(f'3. {third_place}')
