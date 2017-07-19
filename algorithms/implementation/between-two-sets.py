def getTotalX(a, b):
    between = 0
    for i in range(a[-1], b[0] + 1):
        if all(i % x == 0 for x in a) and all(x % i == 0 for x in b):
            between += 1
    return between

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)
