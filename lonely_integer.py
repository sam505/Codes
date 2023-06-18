def lonelyinteger(a):
    for num in a:
        if a.count(num) == 1:
            return num