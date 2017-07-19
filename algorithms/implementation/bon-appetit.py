def bonAppetit(n, k, b, ar):
    b0 = 0
    for i in range(n):
        if i == k:
            continue
        else:
            b0 += ar[i]
    if b - (b0 // 2) != 0:
        return b - b0 // 2
    return "Bon Appetit"
        

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
