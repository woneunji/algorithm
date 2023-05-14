def solution(n):
    answer = 0
    m = n // 2 + 1
    if (n % 2):
        for i in range(m):
            answer += (2 * i +1)
    else:
        for i in range(m):
            answer += ((2 * i) ** 2)
    return answer