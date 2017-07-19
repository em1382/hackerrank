def sockMerchant(n, ar):
    socks = set()
    pairs = 0
    
    for sock in ar:
        if sock in socks:
            pairs += 1
            socks.remove(sock)
        else:
            socks.add(sock)
    return pairs
        

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
