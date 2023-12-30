n = int(input())
rows = []
row = []
counter = 0
step = 1


def print_line(line, w):
    spaces = w - len(line)
    left = spaces // 2
    right = spaces - left
    print(' ' * left + line + ' ' * right)


for x in range(1, n + 1):
    # Добавлять x в row
    # Проверка полностью ли сформирована строка
    if counter == step:
        rows.append(row)
        row = []
        counter = 0
        step += 1
    row.append(str(x))
    counter += 1
rows.append(row)


last_line = ' '.join(rows[-1])
width = len(last_line)


for row in rows:
    print_line(' '.join(row), width)
