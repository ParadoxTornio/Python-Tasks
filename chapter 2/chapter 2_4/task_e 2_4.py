n = int(input())
counter = 0

for i in range(n):
    zayka = 0
    while (string := input()) != 'ВСЁ':
        if string == 'зайка':
            zayka = 1
    counter += zayka

print(counter)
