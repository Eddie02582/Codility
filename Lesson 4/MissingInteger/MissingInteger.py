
    
def solution(A):
    # write your code in Python 3.6    
    appear=[False]*len(A)
    for x in A:
        if x<=len(A) and x>0:
            appear[x-1]=True 
    for i,bapper in enumerate(appear,1):
        if not bapper:
            return i;    
    return len(A)+1
    
    
    
