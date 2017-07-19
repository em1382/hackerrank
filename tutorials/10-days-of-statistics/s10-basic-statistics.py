import numpy
from scipy import stats

n = int(input())
nums = [int(x) for x in input().split()]

print(numpy.mean(nums))
print(numpy.median(nums))
print(*stats.mode(nums)[0])
