def solution(A, K): 
	if not A:
        return []
    
	K = K % len(A)
    m = len(A)
	return  A[m - K:]+A[:m - K] 

	
	
def solution(A, K):
    # write your code in Python 3.6
    if not A:
        return A
        
    K = K % len(A)
    
    for i in range(K):
        A = A[-1:] + A[:-1]
    return A	

	
