def solution(A):
    # write your code in Python 3.6
    
    res = (1 + len(A) + 1)*(len(A) + 1) //2
    
    for n in A:
        res -= n    
    return res