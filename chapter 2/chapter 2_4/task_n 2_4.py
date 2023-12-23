n = int(input())
m = int(input())
max_num_len = len(str(n * m))

for y in range(n):
    if y % 2 == 0:
        for x in range(m):
            print(str(y * m + x + 1).rjust(max_num_len), end=' ')
    else:
        for x in range(m - 1, -1, -1):
            print(str(y * m + x + 1).rjust(max_num_len), end=' ')
    print()
