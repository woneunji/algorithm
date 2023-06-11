def solution(my_string, s, e):
    tmp = my_string[s:e+1]
    tmp = tmp[::-1]
    return my_string[:s] + tmp + my_string[e+1:]