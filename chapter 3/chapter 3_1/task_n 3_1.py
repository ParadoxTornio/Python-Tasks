numbers = input()
list_of_numbers = numbers.split()

m = int(input())

for i in list_of_numbers:
    print(int(i) ** m, end=' ')
