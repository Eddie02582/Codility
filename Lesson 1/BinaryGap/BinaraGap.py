# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

		
		
def solution(N):
    bin_array=(bin(N)[2:]+'e').split('1') 
    result=[ len(x) for x in bin_array if x !="" and 'e' not in x]
    return  max(result) if  result else 0
	
def solution(N):
    strbin=bin(N)[2:]
    left,max,right=0,0,0
    for index,s in enumerate(strbin):
        if s=='1':
            left=right
            right=index	
            max = right-left-1 if max <right-left-1 else max 	
    return  max