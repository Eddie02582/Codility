def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0
    result ,min_buy = 0,float('inf')
    for i in range(len(A)):
        min_buy = min(A[i],min_buy)
        result = max(0,A[i] - min_buy)
    
    return result