def slow_max_slice(A):
    n = len(A)
    result = 0
    for p in range(n):
        for q in range(p, n):
            sum = 0
            for i in range(p, q + 1):
                sum += A[i]
                result = max(result, sum)
    return result 
            
            
def quadratic_max_slice_pref(A):
    n ,result = len(A), 0
    pref = [0] * (n + 1)
    for i in range(1,n + 1):
        pref[i] = pref[i - 1] + A[i - 1]

    for p in range(n):
        for q in range(p, n):
            sum = pref[q + 1] - pref[p]
            result = max(result, sum)
    return result
    
def quadratic_max_slice(A):
    n ,result = len(A), 0
    for p in range(n):
        sum = 0
        for q in range(p, n):
            sum += A[q]
            result = max(result, sum)
    return result
    
def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice   

def max_slice(A):
    res,temp = 0,0
    for a in A:
        temp += a
        if temp < 0:
            temp = 0
        res = max(temp,res)
    return res

A = [5,-7,3,5,-2,4,-1]
slow_max_slice(A)
quadratic_max_slice_pref(A)
quadratic_max_slice(A)
golden_max_slice(A)
max_slice(A)