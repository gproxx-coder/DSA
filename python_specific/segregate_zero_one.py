arr = [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0]


def segregate(arr):
    sm = 0
    n = len(arr)
    for num in arr:
        sm += num

    newarr = []
    newarr.extend([0]*(n-sm))
    newarr.extend([1]*sm)
    print(newarr)


segregate(arr)
