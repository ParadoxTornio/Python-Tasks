n = int(input())
step = 1
counter = 0

for i in range(1, n + 1):
    print(i, end=' ')
    counter += 1
    if counter == step:
        print()
        counter = 0
        step += 1
