n1 = int(input())
n2 = int(input())
result_of_units = (n1 % 10 + n2 % 10) % 10
result_of_tens = (n1 // 10 % 10 + n2 // 10 % 10) % 10
result_of_hundreds = (n1 // 100 + n2 // 100) % 10
print(result_of_hundreds * 100 + result_of_tens * 10 + result_of_units)
