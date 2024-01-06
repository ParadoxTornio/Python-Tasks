n = int(input())
list_of_strings = []

for i in range(n):
    string = input()
    list_of_strings.append(string)

target = input()
target = target.lower()

for string in list_of_strings:
    new_string = string.lower()
    if new_string.find(target) != -1:
        print(string)
