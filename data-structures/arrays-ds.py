n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
[print(x, end=' ') for x in arr[::-1]].strip()
