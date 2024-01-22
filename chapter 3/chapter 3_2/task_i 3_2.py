counter = {}

while (string := input()) != '':
    string = string.split()
    for word in string:
        counter[word] = counter.get(word, 0) + 1

for name, amount in counter.items():
    print(f'{name} {amount}')
