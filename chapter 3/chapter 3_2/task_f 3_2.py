n1 = int(input())
n2 = int(input())
set1 = set()

for i in range(n1 + n2):
    string = input()
    if string in set1:
        set1.remove(string)
    else:
        set1.add(string)

if len(set1) != 0:
    for name in sorted(set1):
        print(name)
else:
    print('Таких нет')
