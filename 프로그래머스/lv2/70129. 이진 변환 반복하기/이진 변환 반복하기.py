def solution(s):
    cnt = 0
    ncnt = 0
    while s != "1" : 
        cnt = cnt + s.count("0")
        s = s.replace("0", "")
        s_len = len(s)
        s = format(len(s), 'b')
        s = str(s)
        ncnt+=1
        
    return [ncnt,cnt]