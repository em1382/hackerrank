S = input().strip()
original = 'SOS' * (len(S) // 3)
changed = 0
for n, o in zip(S, original):
    if n != o:
        changed += 1
print(changed)
