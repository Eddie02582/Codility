#https://app.codility.com/demo/results/training63W4FX-TU6/

def solution(A):
    # write your code in Python 3.6
    result,temp  = float('-inf'),0
    for n in A:
        temp += n
        result = max(result,temp)
        if temp < 0:
            temp = 0
    return result
    
def solution(A):
    # write your code in Python 3.6
    result,temp  = float('-inf'),0
    for n in A:
        if temp < 0:
            temp = 0    
        temp += n
        result = max(result,temp)
    return result