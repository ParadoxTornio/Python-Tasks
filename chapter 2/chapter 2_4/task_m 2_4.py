n = int(input())
m = int(input())
max_num_len = len(str(n * m))

for y in range(n):
    for x in range(m):
        print(str(x * n + y + 1).rjust(max_num_len), end=' ')
    print()
