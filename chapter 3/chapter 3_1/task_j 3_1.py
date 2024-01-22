counter = {}

while (string := input()) != 'ФИНИШ':
    string = string.replace(' ', '')
    string = string.lower()
    for symb in string:
        counter[symb] = counter.get(symb, 0) + 1

max_frequency = max(counter.values())
symbols = []
for symb, freq in counter.items():
    if freq == max_frequency:
        symbols.append(symb)

symbols.sort()

print(symbols[0])
