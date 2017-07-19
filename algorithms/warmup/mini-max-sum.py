arr = list(map(int, input().strip().split(' ')))
arr.sort()

min_sum = 0
max_sum = 0

for i in range(4):
    max_sum += arr[-i - 1]
    min_sum += arr[i]

print(min_sum, max_sum)
