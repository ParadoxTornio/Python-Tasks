n1 = int(input())
n2 = int(input())
n3 = int(input())
first_place = max(n1, n2, n3)
third_place = min(n1, n2, n3)
second_place = n1 + n2 + n3 - first_place - third_place
if first_place == n1:
    first_place = 'Петя'
elif first_place == n2:
    first_place = 'Вася'
elif first_place == n3:
    first_place = 'Толя'
if second_place == n1:
    second_place = 'Петя'
elif second_place == n2:
    second_place = 'Вася'
elif second_place == n3:
    second_place = 'Толя'
if third_place == n1:
    third_place = 'Петя'
elif third_place == n2:
    third_place = 'Вася'
elif third_place == n3:
    third_place = 'Толя'

print(f'          {first_place}          ')
print(f'  {second_place}  ')
print(f'                  {third_place}')
print('   II      I      III   ')
