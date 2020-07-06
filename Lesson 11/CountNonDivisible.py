#https://app.codility.com/demo/results/trainingNC2XD6-6JW/
# 55
def solution(A):
    res = []
    for i in range(len(A)):
        count = 0
        for j in range(len(A)):
            if i != j and A[i] % A[j] != 0:
                count += 1
        res.append(count)
    return res
    
    
    
solution([3,1,2,3,6])