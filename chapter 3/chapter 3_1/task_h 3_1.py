n = int(input())

for i in range(n):
    string = input()
    if string.find('зайка') != -1:
        print(string.find('зайка') + 1)
    else:
        print('Заек нет =(')
