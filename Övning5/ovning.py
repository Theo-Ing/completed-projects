bin_cache = {}
def pascal(n, k):
    key = str(str(n) + ":" + str(k))
    if k > n:
        print("Invalid input")
        return
    if key in bin_cache:
        return bin_cache[key]
    elif k == 1 or k == n - 1:
        return n
    elif k == n or k == 0 or n == 0 or n == 1:
        return 1
    else:
        binCoeff = pascal(n-1, k) + pascal(n-1, k-1)
        bin_cache[key] = binCoeff
        return binCoeff

pascal(100, 49)
