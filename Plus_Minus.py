def plus_minus(arr):
    p = 0
    n = 0
    z = 0
    for i in arr:
        if i == 0:
            z += 1
        elif i >= 1:
            p += 1
        elif i < 0:
            n += 1
    print("{:.6f}".format(p / len(arr)))
    print("{:.6f}".format(n / len(arr)))
    print("{:.6f}".format(z / len(arr)))

arr = [1, 1, 0, -1, -1]
plus_minus(arr)
