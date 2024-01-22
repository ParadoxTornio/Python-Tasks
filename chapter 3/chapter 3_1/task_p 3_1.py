w = int(input()) - 3
n = int(input())
list_of_strings = []
new_strings = []

for i in range(n):
    string = input()
    list_of_strings.append(string)

for string in list_of_strings:
    if len(string) < w:
        new_strings.append(string)
        w -= len(string)
    else:
        new_string = ''
        new_string += string[:w]
        new_string += '...'
        new_strings.append(new_string)
        break

for string in new_strings:
    print(string)
