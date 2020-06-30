def solution(A):
    # write your code in Python 3.6
    numbers = set(A)    
    for i in range(1,len(A) + 1):
        if i not in numbers:
            return 0
    
    return 1   
