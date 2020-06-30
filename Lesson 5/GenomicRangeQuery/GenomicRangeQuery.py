#O(N + M)
def solution(S, P, Q):
    score = {'A':1,'C':2,'G':3,'T':4}
    res = []
    for p,q in (zip(P,Q)):
        s = S[p : q + 1]
        for key in score.keys():
            if key in s:
                res.append(score[key])
                break
    
    return res