def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0
    
    right = sum(A)
    left = 0
    res = float('inf')
    for i in range(len(A) - 1):
        right -= A[i]
        left  += A[i]
        res = min(res,abs( right - left))
    return res
