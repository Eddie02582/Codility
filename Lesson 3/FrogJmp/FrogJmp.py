def solution(X, Y, D):
    n ,res = divmod(Y - X,D)
    if res:
        n += 1
    return n