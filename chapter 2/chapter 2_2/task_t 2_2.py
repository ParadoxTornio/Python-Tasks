n1 = input()
n2 = input()
n3 = input()

line_with_hare = None

if 'зайка' in n1:
    line_with_hare = n1
if 'зайка' in n2:
    if line_with_hare is None:
        line_with_hare = n2
    else:
        line_with_hare = min(n2, line_with_hare)
if 'зайка' in n3:
    if line_with_hare is None:
        line_with_hare = n3
    else:
        line_with_hare = min(n3, line_with_hare)

print(f'{line_with_hare} {len(line_with_hare)}')
