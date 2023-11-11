n = int(input())
m = int(input())
t = int(input())
result_of_sum_type = n * 60 + m + t
hours = result_of_sum_type // 60 % 24
minutes = result_of_sum_type % 60
print(f'{hours // 10}{hours % 10}:{minutes // 10}{minutes % 10}')
