def countPatterns(n):
    result = 24**n - (9 * 8**n - 9*2**n - 18*3**n + 24)
    mod = 10 ** 9 + 7
    return result % mod
