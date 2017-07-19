from collections import deque
nd = [int(x) for x in input().split()]
d = deque([int(x) for x in input().split()])
d.rotate(-nd[1])
[print(i, end=' ') for i in d]
