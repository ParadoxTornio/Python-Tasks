ans = -1
prev_h = 0
n = int(input())

for i in range(n):
    b = int(input())
    h = b % 256
    if h >= 100:
        ans = i
        break
    b //= 256
    r = b % 256
    m = b // 256
    true_h = (37 * (m + r + prev_h)) % 256
    if h != true_h:
        ans = i
        break
    prev_h = h

print(ans)
