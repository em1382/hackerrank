n = int(input())
A = sorted(int(x) for x in input().split())
min_diff = A[1] - A[0]
pairs = []
for i in range(2, len(A) - 1):
    diff = A[i + 1] - A[i]
    if diff < min_diff:
        min_diff = diff
        pairs = []
    if diff == min_diff:
        pairs += [A[i], A[i + 1]]
print(*pairs)
