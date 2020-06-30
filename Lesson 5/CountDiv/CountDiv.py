def solution(A, B, K):
    # write your code in Python 3.6
    add = 1 if A % K == 0 else 0
    res = (B//K) - (A//K) + add
    return res
