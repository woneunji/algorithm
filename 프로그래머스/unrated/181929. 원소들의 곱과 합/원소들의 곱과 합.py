def solution(num_list):
    a1 = 1
    a2 = 0
    for i in range(len(num_list)):
        a1 *= num_list[i]
        a2 += num_list[i]
    a2 = a2**2
    if (a1 < a2):
        return 1
    else:
        return 0