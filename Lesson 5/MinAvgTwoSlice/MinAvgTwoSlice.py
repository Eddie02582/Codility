def solution(A):
    # write your code in Python 3.6
    N = len(A)  
    minAvg  = float('inf')
    minSliceIndex  = 0
        
    for i in range(N - 1):   
        avg =  (A[i] + A[i + 1]) / 2
        if avg < minAvg :
            minAvg  = avg
            minSliceIndex  = i
        
        if i < N - 2:           
            avg = (A[i] + A[i + 1] + A[i + 2]) / 3
            if avg < minAvg:
                minAvg = avg
                minSliceIndex = i
    return minSliceIndex  
    