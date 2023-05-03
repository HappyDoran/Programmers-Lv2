def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    return a * b / gcd(a, b)

def solution(arr):
    answer = 0
    stack = []
    for i in arr:
        if not stack:
            stack.append(i)
        else:
            stack.append(int(lcm(stack.pop(), i)))
    
    return stack[len(stack)-1]
    