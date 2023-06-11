def solution(my_strings, parts):
    answer = ''
    n = 0
    for i in my_strings:
        s = parts[n][0]
        l = parts[n][1] + 1
        tmp = i[s:l]
        answer += tmp
        n += 1
    return answer