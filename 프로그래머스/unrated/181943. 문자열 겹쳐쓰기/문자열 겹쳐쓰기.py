def solution(my_string, overwrite_string, s):
    l = s + len(overwrite_string)
    s1 = my_string[:s]
    s2 = my_string[l:]
    answer = s1 + overwrite_string + s2
    return answer