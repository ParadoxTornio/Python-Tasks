n = int(input())

preferences = {}

for i in range(n):
    string = input()
    string = string.split()
    name = string[0]
    for preference in string[1:]:
        preferences[preference] = preferences.get(preference, []) + [name]

target = input()

if target in preferences:
    print('\n'.join(sorted(preferences[target])))
else:
    print('Таких нет')
