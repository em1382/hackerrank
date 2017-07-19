miles, eaten = 0, 0
n = int(input().strip()) - 1
calories = sorted(list(map(int, input().strip().split(' '))))
while n > -1:
    miles += (calories[n] * 2**eaten)
    eaten += 1
    n -= 1
print(miles)
