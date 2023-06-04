def solution(my_string, queries):
    for i in queries:
        my_string = list(my_string)
        temp = (my_string[i[0]:i[1]+1])[::-1]
        my_string[i[0]:i[1]+1] = temp
        my_string = ''.join(my_string)
    return my_string