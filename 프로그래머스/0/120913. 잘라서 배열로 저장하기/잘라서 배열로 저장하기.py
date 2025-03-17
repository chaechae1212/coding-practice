def solution(my_str, n):
    my=[]
    for i in range(0,len(my_str),n):
        my.append(my_str[i:i+n])
    return my