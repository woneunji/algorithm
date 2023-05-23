def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        temp = []
        for i in range(len(arr)):
            if (s <= i <= e):
                if k < arr[i]:
                    temp.append(arr[i])
        if not temp:
            answer.append(-1)
        else:
            answer.append(min(temp))
    return answer