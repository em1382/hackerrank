n = int(input())
arr = [int(x) for x in input().split()]

left, right, equal = [], [], []
p = arr[0]
for n in arr:
    if n < p:
        left.append(n)
    elif n > p:
        right.append(n)
    else:
        equal.append(n)
print(*(left + equal + right))
