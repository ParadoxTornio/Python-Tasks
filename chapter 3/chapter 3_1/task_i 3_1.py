while True:
    string = input()
    if string == '':
        break
    if string.find('#') == 0:
        continue
    if string.find('#') != -1:
        string = string[:string.find('#')]
    print(string)
