def solution(arr, queries):
    for i in range(len(queries)):
        temp = 0
        temp = arr[queries[i][0]]
        arr[queries[i][0]] = arr[queries[i][1]]
        arr[queries[i][1]] = temp
    return arr