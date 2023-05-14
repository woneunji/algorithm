def solution(a, b):
    answer = 0
    a1 = int(str(a) + str(b))
    a2 = 2 * a * b
    answer = max(a1, a2)
    return answer