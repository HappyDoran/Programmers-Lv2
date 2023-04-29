import math

def solution(n, words):
    answer = []
    turn = 0
    for i in range(len(words)):
        if i != 0 and words[i][0] != words[i-1][-1]:
            turn = i
            # break
        else:
            for j in range(0,i):
                if words[i] == words[j]:
                    turn = i
                    # break
        if turn != 0 :
            break
    # print(turn)
    if turn == 0 :
        answer.append(0)
        answer.append(0)
    else :
        turn = turn + 1
        if turn % n == 0 :
            answer.append(n)
        else:
            answer.append((turn % n))
        answer.append(math.ceil(turn/n))
    return answer