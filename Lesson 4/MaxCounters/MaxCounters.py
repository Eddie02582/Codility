def solution1(N, A):
    # write your code in Python 3.6 O(N * M)    
    max_count = 0
    res = [0] * N
    for n in A:
        if n <= N :
            res[n - 1] += 1
            max_count = max(max_count,res[n - 1])
        else:
            for i in range(len(res)):
                res[i] = max_count    
    return res    
    
def solution(N, A):
    # N + M)    
    max_count = 0
    res = [0] * N
    for n in A:
        if n <= N :
            res[n - 1] += 1
            max_count = max(max_count,res[n - 1])
        else:            
            res = [max_count]* N
    
    return res    
    
    
    
def solution2(N, A):
    # write your code in Python 3.6    
    B=[0]*N
    max=0
    add=0
    for x in A:   
        if x <=N:
            if B[x-1] <add:
               B[x-1]= add+1              
            else:
                B[x-1]+=1  
            max= B[x-1] if B[x-1]> max else max
        else:            
            add=max
     
    for i in range(len(B)):
        if B[i]<add:
            B[i]=add 
    return B
