n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
m = max(height)
if k >= m:
    print(0)
else:
    print(m - k)
