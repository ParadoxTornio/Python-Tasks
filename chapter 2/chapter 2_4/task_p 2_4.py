h = int(input())
w = int(input())


def print_num(num, w):
    spaces = w - len(str(num))
    left = spaces // 2
    right = spaces - left
    print(' ' * left + str(num) + ' ' * right, end='')


for x in range(1, h + 1):
    if x != 1:
        print('-' * w * h + (h - 1) * '-')
    for y in range(1, h + 1):
        print_num(x * y, w)
        if y != h:
            print('|', end='')
    print()
