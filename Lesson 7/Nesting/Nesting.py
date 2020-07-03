# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    match = {')':'('}
   
    stack = []
    for s in S:
        if s in match.values() or not stack:
            stack.append(s)
        elif stack.pop(-1) !=  match[s]:
            return 0
    
    return 1 if len(stack) == 0 else 0