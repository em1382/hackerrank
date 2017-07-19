def solve(n, s, d, m):
    combos = 0
    i = 0
    while i < len(s):
        if sum(s[i:(i + m)]) == d:
            combos += 1
        i += 1
    return combos
        

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
