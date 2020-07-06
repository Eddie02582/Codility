#https://app.codility.com/demo/results/training3F65NU-GPJ/
def solution_onn(A):
    # write your code in Python 3.6
    if len(A) <= 3:
        return 0
    #slice
    res = 0
    for i in range(1,len(A) - 1):
        left,right = A[1:i],A[i + 1: len(A) - 1]
        left_value = getMaxSliceValue(left)
        right_value = getMaxSliceValue(right)
        res = max(left_value + right_value ,res)
    return res


def getMaxSliceValue(A):
    res,temp = 0,0,
    for n in A:
        temp += n
        if temp < 0:
            temp = 0
        res = max(res,temp)
    return res

#https://app.codility.com/demo/results/trainingARPUMH-GPA/
def solution_dp(A):
    # write your code in Python 3.6
    if len(A) <= 3:
        return 0
    #slice
    max_left,max_right,max_slice  = 0,0,0
    center = 1

    for i in range(3,len(A)):
        max_left = max(max_left + A[i - 2], A[i - 2])
        max_right = max(max_right + A[i - 1], A[i - 1], max_left)
        if max_right == A[i - 1]:
            center = i - 2;
        elif max_right == max_left: 
            center = i - 1
        if max_right > max_slice: 
            max_slice = max_right;

    return max_slice

#https://app.codility.com/demo/results/training5HP36X-MRF/
def solution(A):
    n = len(A)
    b = [0] * n
    temp = 0
    for i in range(1,n):
        temp = max(0,temp)
        b[i] = temp 
        temp += A[i]
    
    temp,result  = 0,0
    for i in range(n - 2,0,-1):
        temp = max(0,temp)
        result = max(result, temp + b[i]);
        temp += A[i]
    
    return result










#A = [5, 17, 0, 3]
B = [3,2,6,-1,4,5,-1,2]
#C = [3,2,6,-10,4,5,10,-10,10,20,30]



#solution(A)
solution(B)
#[4,5,10] [10,20,30] =79

solution(C)