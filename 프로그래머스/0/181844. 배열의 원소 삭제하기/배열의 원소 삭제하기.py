def solution(arr, delete_list):
    my=[]
    for i in range(len(arr)):
        if arr[i] not in delete_list:
            my.append(arr[i])
    return my
            