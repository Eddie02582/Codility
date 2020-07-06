def solution__(A):
    from collections import defaultdict
    record =  defaultdict(list)   
    max_value = 0
    if len(A) <= 1:
        return 0


    
    for i in range(len(A)):
        record[A[i]].append(i)
        if len(record[A[i]]) > len(A)//2:
            max_value = A[i]   

    res = 0
    positions = record[max_value]

    for count,position in enumerate(positions,1):
        # maxcount > len(A[:position])//2 ,len(positions) -  maxcount > len(A[position + 1:])//2
        if record[max_value] != A[-1]: 
            if count > (position + 1) // 2 and (len(positions) - count) > (len(A) - position - 1)//2:
                res += 1
    
    return res
    
    
def solution(A):   
    
    count = {}
    record = [0] * len(A)
    max_value = 0
    for i in range(len(A)):
        count[A[i]] = count.get(A[i],0) + 1
        if i == 0 :
            record[0] = A[i]
            max_value = A[i]
        elif count[A[i]] > count[max_value]:
            max_value = A[i] 

        record[i] = max_value
    max_value = 0
    count = {}
    record2 = [0] * len(A)
    for i in range(len(A) - 1,0,-1):
        count[A[i]] = count.get(A[i],0) + 1
        if len(A) - 1 == i :
            record2[i] = A[i]
            max_value = A[i]
        elif count[A[i]] > count[max_value]:
            max_value = A[i] 

        record2[i] = max_value
    return   record  


    
    

    
    
A = [4, 4, 2, 5, 3, 4, 4, 4]  
solution(A)      
#3
