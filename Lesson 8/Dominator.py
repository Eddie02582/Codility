#https://app.codility.com/demo/results/trainingM79STW-DYY/
def solution(A):
    # write your code in Python 3.6
    if not A:
        return -1
    count = {}
    length = len(A) //2
    
    for index,n in enumerate(A):
        if n not in count:
            count[n] = 1
        else:
            count[n] += 1
        if count[n]  > length:
            return  index
    return  -1
