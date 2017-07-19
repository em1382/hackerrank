def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            if (ar[j] + ar[i]) % k == 0:
                count += 1
    return count // 2
                
            

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
