def solution(line):
    answer = []
    s = []
    for i in range(0, len(line)):
        A, B, E = line[i][0], line[i][1], line[i][2]
        for j in range(0, i):
            C, D, F = line[j][0], line[j][1], line[j][2]
            if A*D - B*C != 0:
                X = (B*F - E*D)/(A*D - B*C)
                Y = (E*C - A*F)/(A*D - B*C)
            answer.append([X,Y])
    for i in answer:
        if i[0] % 1 == 0 and i[1] % 1 == 0 :
            s.append([int(i[0]),int(i[1])])
    
    xmin=s[0][0]
    xmax=s[0][0]
    ymin=s[0][1]
    ymax=s[0][1]

    for a,b in s:
        xmin=min(xmin,a)
        xmax=max(xmax,a)
        ymin=min(ymin,b)
        ymax=max(ymax,b)

    answer = []
    for _ in range(ymax-ymin+1):
        klist=[]
        for _ in range(xmax-xmin+1):
            klist.append('.')
        answer.append(klist)
    
    for a,b in s:
        answer[b-ymin][a-xmin]='*'

    answer2=[]
    for i in range(len(answer)):
        klist=''
        for j in range(len(answer[0])):
            klist+=answer[i][j]
        
        answer2.insert(0,klist)

    return answer2

    
    return s