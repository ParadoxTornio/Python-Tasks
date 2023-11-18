n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 >= n2 and n1 >= n3:
    print('Петя')
elif n2 >= n1 and n2 >= n3:
    print('Вася')
elif n3 >= n1 and n3 >= n2:
    print('Толя')
