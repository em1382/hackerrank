import collections

n = int(input())
arr = [int(x) for x in input().split()]

print(n-collections.Counter(arr).most_common()[0][1])
