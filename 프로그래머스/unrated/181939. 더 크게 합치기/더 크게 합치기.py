def solution(a, b):
    answer = 0
    a1 = str(a) + str(b)
    a2 = str(b) + str(a)
    a1 = int(a1)
    a2 = int(a2)
    if a1 > a2:
        answer = a1
    else:
        answer = a2
    return answer