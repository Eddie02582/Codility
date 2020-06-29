# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

		
		
def solution(N):
    bin_array=(bin(N)[2:]+'e').split('1') 
    result=[ len(x) for x in bin_array if x !="" and 'e' not in x]
    return  max(result) if  result else 0
	
def solution(N):
    strbin=bin(N)[2:]
    left,res,right=0,0,0
    for index,s in enumerate(strbin):
        if s == '1':
            left = right
            right = index	
            res = max(right-left-1,res)         
    return  res
    
def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:]
    position = -1
    res = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            if position < 0:
                position = i
            else:
                res = max(res, i - position - 1)
                position = i
    
    return res    