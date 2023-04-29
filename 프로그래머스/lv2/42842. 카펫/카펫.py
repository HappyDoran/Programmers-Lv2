def solution(brown, yellow):
    answer = []
    s = []
    for i in range(1,int((brown + yellow)**(1/2)) + 1):
        if (brown+yellow)%i == 0 :
            answer.append(i)
            answer.append(int((brown+yellow)/i))
    
    # print(answer)
    for i in range(2, len(answer), 2):
        if (answer[i]-2)*(answer[i+1]-2) == yellow:
            s.append(answer[i])
            s.append(answer[i+1])
    
    s.sort()
    s.reverse()
    return s