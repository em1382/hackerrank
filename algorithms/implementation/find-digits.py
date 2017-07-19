import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    digits = [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
    count = 0
    for d in digits:
        if d > 0 and n % d == 0:
            count += 1
    print(count)
