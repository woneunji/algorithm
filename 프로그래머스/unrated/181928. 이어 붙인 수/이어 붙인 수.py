def solution(num_list):
    o = ''
    e = ''
    for i in range(len(num_list)):
        if num_list[i] % 2:
            o += str(num_list[i])
        else:
            e += str(num_list[i])
    return int(o) + int(e)