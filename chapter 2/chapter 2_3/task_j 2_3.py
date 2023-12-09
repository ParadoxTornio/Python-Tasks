running = True
cords = [0, 0]


while running:
    direction = input()
    if direction != 'СТОП':
        number_of_steps = int(input())
        if direction == 'СЕВЕР':
            cords[1] += number_of_steps
        elif direction == 'ВОСТОК':
            cords[0] += number_of_steps
        elif direction == 'ЮГ':
            cords[1] -= number_of_steps
        elif direction == 'ЗАПАД':
            cords[0] -= number_of_steps
    elif direction == 'СТОП':
        print(cords[1])
        print(cords[0])
        break
