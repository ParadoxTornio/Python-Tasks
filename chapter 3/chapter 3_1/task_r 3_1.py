string = input()
length = 0
symbol = string[0]

for i in string:
    if symbol == i:
        length += 1
    else:
        print(symbol, length)
        length = 1
        symbol = i

print(symbol, length)
