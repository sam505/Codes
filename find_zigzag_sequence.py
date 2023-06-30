def findZigZagSequence(a, n):
    a.sort()
    print('original:', a)
    mid = int((n)/2)
    a[mid], a[n-1] = a[n-1], a[mid]
    print('exchanged:', a)

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1
    print(a, st, mid)

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return a