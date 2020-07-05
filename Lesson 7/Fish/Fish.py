#https://app.codility.com/demo/results/trainingCPZD8B-NQP/
def solution(A, B):
    mapping = {}
    for i in range(len(A)):
        mapping[A[i]] = B[i]
    res = []

    for i in range(len(A)):
        if not res :
            res.append(A[i])     
        elif B[i] == 0 and mapping[res[-1]] == 1:            
            while res and mapping[res[-1]] == 1 and A[i] > res[-1]:                
                res.pop(-1)  
            if not res  or mapping[res[-1]] == 0 or  A[i] > res[-1]:
                res.append(A[i])  
 
        else:
            res.append(A[i])  
    return len(res)        
