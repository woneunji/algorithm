def solution(my_string, is_prefix):
    for i in range(len(my_string)):
        if is_prefix == my_string[:i]:
            answer = 1
            break
        else:
            answer = 0
    return answer