def solution(s):
    answer = 0
    L = []
    for i in s :
        if len(L) == 0 :
            L.append(i)
        else:
            if L[-1] == i :
                L.pop()
                # print(L)
            else :
                L.append(i)
                # print(L)
    if len(L)==0:
        answer = 1
        
    return answer