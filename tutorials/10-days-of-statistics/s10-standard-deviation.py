import math

n = int(input())
nums = [int(x) for x in input().split()]

print(math.sqrt(sum((x-sum(nums)/len(nums))**2 for x in nums)/len(nums)))
