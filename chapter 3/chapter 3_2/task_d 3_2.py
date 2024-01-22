n1 = int(input())
n2 = int(input())
set1 = set()
set2 = set()
counter = 0

for i in range(n1):
    string = input()
    set1.add(string)

for i in range(n2):
    string = input()
    set2.add(string)

counter += len(set1 & set2)

if counter != 0:
    print(counter)
else:
    print('Таких нет')
