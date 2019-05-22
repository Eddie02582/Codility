def solution(A, K): 
	if A:
		move=K%len(A)
		return  A[len(A)-move:]+A[:len(A)-move] 
	else:		
		return  []
	
	
	

	
