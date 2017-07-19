from collections import Counter

def migratoryBirds(n, ar):
    return max(Counter(ar).most_common(), key=lambda x: x[1])[0]
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
