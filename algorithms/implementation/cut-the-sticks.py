n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

while len(arr) > 0:
    print(len(arr))
    new = []
    min_stick = min(arr)
    for stick in arr:
        if stick > min_stick:
            new.append(stick - min_stick)
    arr = new
