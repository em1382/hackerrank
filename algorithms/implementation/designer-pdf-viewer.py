h = list(map(int, input().strip().split(' ')))
word = input().strip()
max_height = 0
for char in word:
    height = h[ord(char) - 97]
    if height > max_height:
        max_height = height
print(len(word) * max_height)
