n = int(input())
path = input().strip()
y = valleys = 0
for step in path:
    if step == 'U':
        y += 1
        if y == 0:
            valleys += 1
    elif step == 'D':
        y -= 1
print(valleys)
