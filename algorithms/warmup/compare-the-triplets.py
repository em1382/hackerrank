#!/bin/python3

import sys


a0,a1,a2 = input().strip().split(' ')
a = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b = [int(b0),int(b1),int(b2)]

alice = 0
bob = 0

for i in range(len(a)):
    if a[i] > b[i]:
        alice += 1
    elif a[i] < b[i]:
        bob += 1
        
print("{0} {1}".format(alice, bob))
