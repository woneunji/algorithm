def solution(n):
    answer = []
    while n != 1:
        answer.append(n)
        if not (n % 2):
            n = n / 2
            if n == 1:
                answer.append(n)
        else:
            n = 3 * n + 1
            if n == 1:
                answer.append(n)
    return answer