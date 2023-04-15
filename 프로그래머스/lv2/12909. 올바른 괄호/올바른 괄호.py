def solution(s):
    answer = True
    stack = []
    if s[0] == ")":
        return False
    for i in s:
        if i=='(':
            stack.append(i)
        elif i == ")" and len(stack) != 0:
            stack.pop()
        # print(stack)
    if len(stack) > 0 :
        return False
    else :
        return True