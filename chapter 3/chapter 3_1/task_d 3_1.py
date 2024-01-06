while True:
    string = input()
    if string == '':
        break
    if string.endswith('@@@'):
        continue
    if string.startswith('##'):
        string = string[2:]
    print(string)
