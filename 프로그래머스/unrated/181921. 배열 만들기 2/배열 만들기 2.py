def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if i % 5 == 0:
            num = str(i)
            if ("5" or "0") in num:
                answer.append(i)
                for j in num:
                    if not (j == "5" or j == "0"):
                        answer.remove(i)
                        break
    if answer == []:
        return [-1]
    return answer