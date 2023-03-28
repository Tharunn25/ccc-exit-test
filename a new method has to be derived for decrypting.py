def findIndices(n, query):
    arr = [None] * n
    for L, R in query:
        s = sum(arr[L:R+1])
        if arr[L] is None:
            arr[L] = s - sum(arr[:L])
        for i in range(L+1, R+1):
            if arr[i] is None:
                arr[i] = s - arr[i-1]
    X = [i for i in range(n) if arr[i] is not None]
    return sorted(X) if X else [-1]
