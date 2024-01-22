n = int(input())
sett = set()


for i in range(n):
    string = input()
    strings = string.split()
    sett |= set(strings)

for i in sett:
    print(i)
