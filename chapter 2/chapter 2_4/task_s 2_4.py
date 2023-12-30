def print_line(max_num, n, width):
    center_size = n - 2 * (max_num - 1)
    for i in range(1, max_num):
        print(str(i).rjust(width), end=' ')
    for i in range(center_size):
        print(str(max_num).rjust(width), end=' ')
    for i in range(max_num - 1, 0, -1):
        print(str(i).rjust(width), end=' ')
    print()


n = int(input())
max_number = (n + 1) // 2
width = len(str(max_number))
if n % 2 == 0:
    for i in range(1, max_number + 1):
        print_line(i, n, width)
    for i in range(max_number, 0, -1):
        print_line(i, n, width)
else:
    for i in range(1, max_number):
        print_line(i, n, width)
    print_line(max_number, n, width)
    for i in range(max_number - 1, 0, -1):
        print_line(i, n, width)
