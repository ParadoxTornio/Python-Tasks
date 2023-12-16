left = 1
right = 1000

while left <= right:
    mid = (right + left + 1) // 2
    print(mid)
    answer = input()
    if answer == 'Угадал!':
        break
    elif answer == 'Больше':
        left = mid + 1
    else:
        right = mid - 1
