def solution(A):
    # write your code in Python 3.6
    SetNumbers=set(A)
    if len(set(A))!=len(A):
        return 0
    sum=0
    for i,value in enumerate(A,1):
        sum^=value
        sum^=i
    
    return 1 if sum == 0 else 0;   
