def stack(hello):
    stack = []
    for j in range(len(hello)):
        if hello[j] == "[" or hello[j] == "(" or hello[j] == "{":
            stack.append(hello[j])
        elif len(stack) != 0 and hello[j] == "]" and stack[-1] == "[":
            stack.pop()
        elif len(stack) != 0 and hello[j] == ")" and stack[-1] == "(":
            stack.pop()   
        elif len(stack) != 0 and hello[j] == "}" and stack[-1] == "{":
            stack.pop()
        else :
            return 0
    if len(stack) == 0 :
        return 1
    else :
        return 0
    
def solution(s):
    answer = 0
    # print(s[-1])
    for i in range(0,len(s)):
        hello = []
        for j in range(0,len(s)):
            hello.append(s[j-i])
        if stack(hello) == 1 :
            answer+=1
        
    return answer