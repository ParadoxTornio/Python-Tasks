n = int(input())
name = input()
min_name = name

for i in range(n - 1):
    # min_name = min(min_name, input())
    name = input()
    if min_name > name:
        min_name = name

print(min_name)
