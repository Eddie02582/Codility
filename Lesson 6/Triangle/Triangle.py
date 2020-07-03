# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#Detected time complexity:O(N*log(N))
def solution(A):
    # write your code in Python 3.6
    if len(A) < 3:
        return 0
    A.sort()
    for i in range(len(A) - 2):
        if A[i] > 0 and A[i] + A[i + 1] > A[i + 2]:
            return 1
    return 0