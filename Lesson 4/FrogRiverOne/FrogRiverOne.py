def solution(X, A):
    numbers = set()
    for i,n in enumerate(A):
        numbers.add(n)
        if len(numbers) == X:
            return i
    
    return - 1
    
    
def solution(X, A):
    exist = [False] * X
    count = 0
    for i,n in enumerate(A):
        if not exist[n - 1]:
            count += 1
        exist[n - 1] = True
        if count == X:
            return i
    
    return -1
