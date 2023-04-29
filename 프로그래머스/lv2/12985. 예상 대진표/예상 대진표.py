import math

def solution(n,a,b):
    answer = 0
    round = 1
    while math.ceil(a/2) != math.ceil(b/2):
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        round+=1
        print(a,b,round)
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')
    
    return round