#https://app.codility.com/demo/results/training4BYA67-TJU/
def solution(N):
    count,i = 0,1
    
    while (i * i < N):
        if N % i == 0:
            count += 2
        i += 1
    
    if i * i == N:
        count += 1    
    return count 

