running = True
counter = 0
while running:
    n = input()
    if n == 'Приехали!':
        print(counter)
        running = False
    else:
        if 'зайка' in n:
            counter += 1
