def solution(X, A):
	S = set()
	count = len(A)
	for i in range(0, count):
		S.add(A[i])
		if(len(S) == X):
			return i
	return -1
    
    
def solution2(X, A):
    tiles=[Fasle]*X
    count=0  
    for i,value in enumerate(A)	
        index=value-i
        if index<X and !tiles[index]:
            count+=1
            tiles[index]=True
        if todo==X:		
            return i
	return -1
    
