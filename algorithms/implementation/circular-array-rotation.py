from collections import deque


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = deque([int(a_temp) for a_temp in input().strip().split(' ')])
for i in range(k):
    a.rotate(1)
for a0 in range(q):
    m = int(input().strip())
    print(a[m])
