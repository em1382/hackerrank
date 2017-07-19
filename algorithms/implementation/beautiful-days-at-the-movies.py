i, j, k = [int(x) for x in str(input()).strip().split()]
beautiful = 0
for x in range(i, j + 1):
    if abs(x - int(str(x)[::-1])) % k == 0:
        beautiful += 1

print(beautiful)
