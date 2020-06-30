  
def solution(A):
    # write your code in Python 3.6
    numbers = set()
    for n in A:
        numbers.add(n)
        
    for i in range(1,len(A) + 1):
        if i not in numbers:
            return i
    
    return len(A) + 1    
    
