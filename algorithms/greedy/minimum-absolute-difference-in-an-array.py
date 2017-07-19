n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
a.sort()
min_diff = abs(a[0] - a[1])
for i in range(n - 1):
    diff = abs(a[i + 1] - a[i])
    if diff < min_diff:
        min_diff = diff
print(min_diff)
