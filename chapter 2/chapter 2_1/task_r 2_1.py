binary_numbers = {
    '0': 0,
    '1': 1,
    '10': 2,
    '11': 3,
    '100': 4,
    '101': 5,
    '110': 6,
    '111': 7,
    '1000': 8,
    '1001': 9
}
n = input()
n_list = list(n)
price = 0
m = int(input())
for i in range(len(n_list)):
    price += binary_numbers.get(n_list[i])
print(price)
