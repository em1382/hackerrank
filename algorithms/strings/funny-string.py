def funnyString(s):
    r = s[::-1]
    for i in range(1, len(s)):
        if not abs(ord(s[i]) - ord(s[i - 1])) == abs(ord(r[i]) - ord(r[i - 1])):
            return "Not Funny"
    return "Funny"

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
