import math

people = 5
liked = 0
for day in range(int(input())):
    people = math.floor(people / 2)
    liked += people
    people *= 3
print(liked)
