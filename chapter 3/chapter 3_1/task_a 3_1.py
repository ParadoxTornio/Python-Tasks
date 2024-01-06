n = int(input())
counter = 0

for i in range(n):
    string = input()
    if string[0] == 'а' or string[0] == 'б' or string[0] == 'в':
        counter += 1

if counter == n:
    print('YES')
else:
    print('NO')
