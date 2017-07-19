import re

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    if re.search(r'h.*a.*c.*k.*e.*r.*r.*a.*n.*k', s):
        print('YES')
    else:
        print('NO')
