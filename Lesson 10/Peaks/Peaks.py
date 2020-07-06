#https://app.codility.com/demo/results/training47QM4V-SAC/
def solution(A):
    peak = []
    n = len(A) - 1
    for i in range(1,n):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peak.append(i)
            
    i = 0
    while i 