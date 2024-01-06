length = int(input())
n = int(input())

for i in range(n):
    string = input()
    if len(string) > length:
        string = string[:length - 3]
        string += '...'
    print(string)
