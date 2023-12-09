running = True
summa = 0
while running:
    n = float(input())
    if n == 0:
        running = False
    else:
        if n >= 500:
            summa += n - n * 0.1
        else:
            summa += n
print(summa)
