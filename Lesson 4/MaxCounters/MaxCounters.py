def solution1(N, A):
    # write your code in Python 3.6    
    B=[0]*N
    max=0
    for x in A:   
        if x <=N:            
            B[x-1]+=1
            max= B[x-1] if B[x-1]> max else max
        else:
            B=[max]*N
    return B
    
    
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
