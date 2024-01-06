n = int(input())
counter = 0

for i in range(n):
    string = input()
    counter += string.count('зайка')

print(counter)
