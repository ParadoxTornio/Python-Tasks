n = int(input())
m = int(input())
max_num_len = len(str(n * m))
d = 2 * n - 1

for y in range(n):
    start = y + 1
    for x in range(m):
        print(str(start).rjust(max_num_len), end=' ')
        if x % 2 == 0:
            start += d - y * 2
        else:
            start += 1 + y * 2

    print()
