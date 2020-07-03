#O(N) or O(N**2) 92%
#https://app.codility.com/demo/results/trainingZVQ9K2-347/
def solution_(H):
    exist = set()
    count = 0    
    for i in range(len(H)):    
        if H[i] not in exist:
           count += 1         
        else:
            prev = i - 1 
            while prev >= 0 and H[prev] != H[i]:
                if H[prev] < H[i]:
                    count += 1                 
                    break
                prev -= 1
        exist.add(H[i]) 
    return count    
        

#https://app.codility.com/demo/results/trainingQ5RQP7-SY8/
def solution(H):
    stack = [0] * 100000
    stackSize,ans  = 0,0
    for i in range(len(H)):    
        while  stackSize > 0 and H[i] < stack[stackSize - 1]:
            stackSize -= 1
            ans += 1
        if (stackSize <= 0 and H[i] > 0) or H[i] > stack[stackSize - 1] :      
            stack[stackSize] = H[i];
            stackSize += 1
    return ans + stackSize


solution([8,8,5,7,9,8,7,4,8])
solution([8])
solution([8,4,8,9,8])

#[8,5,7,9,8,4,8]


 
