#https://app.codility.com/demo/results/trainingB42CEC-7J7/
def solution(A):
    peak = []
    n = len(A) - 1
    for i in range(1,n):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peak.append(i)
    
    res = 0
    for i in range(1,len(peak) + 1):
        count,prev  = 1 ,peak[0]
        for j in range(1,len(peak)):
            if peak[j] - prev >= i:
                count += 1
                prev = peak[j]
            if i == count:
                break

        if count >= i:
            count = i
        res = max(res,count)

    return res
        
        
        
A = [1,5,3,4,3,4,1,2,3,4,6,2]        
solution (A)