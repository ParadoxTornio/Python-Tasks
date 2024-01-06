n = int(input())
list_of_numbers = []

for i in range(n):
    number = int(input())
    list_of_numbers.append(number)

m = int(input())

for i in list_of_numbers:
    print(i ** m)
