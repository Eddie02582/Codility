def solution(A):
    # write your code in Python 3.6
    count = set()
    for n in A:
        count.add(n)
    
    return len(count)