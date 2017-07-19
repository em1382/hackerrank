#!/bin/python3
z, p, n = 0, 0, 0
s = int(input())
l = [int(x) for x in str(input()).split(" ")]
for i in l:
    if i > 0:
        p += 1
    elif i == 0:
        z += 1
    else:
        n += 1
        
print(p/s)
print(n/s)
print(z/s)
