def solution(N):
    factor = []
    i = 1
    while i * i < N:
        n,res = divmod(N,i)
        if res == 0:
            factor.append((i,n))
        i += 1
        
    if i * i == N:
        factor.append((i,i))

        
    A,B = factor[-1]
    return 2 * (A + B)