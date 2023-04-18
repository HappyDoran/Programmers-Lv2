def fivo(n):
    fx,fy = 0,1
    for i in range(n):
        fx,fy = fy,fx+fy
    return fx

def solution(n):
    answer = 0
    if fivo(n) < 1234567 :
        return fivo(n)
    else:
        return fivo(n)%1234567