n = int(input())
list_of_porridges = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']

for i in range(n):
    i %= 5
    print(list_of_porridges[i])
