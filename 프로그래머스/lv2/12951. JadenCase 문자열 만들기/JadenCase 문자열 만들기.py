def solution(s):
    answer = s.split(" ")
    array = []
    for i in answer :
        i = i.capitalize()
        array.append(i)
    array = " ".join(array)
    return array