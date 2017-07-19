n, k = (int(x) for x in input().split())
prices = sorted(int(p) for p in input().split())
toys = 0
for i in range(n - 1):
    if prices[i] > k:
        break
    else:
        k -= prices[i]
        toys += 1
print(toys)
