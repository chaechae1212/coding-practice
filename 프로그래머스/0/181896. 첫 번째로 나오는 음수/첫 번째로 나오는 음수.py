def solution(num_list):
    num=-1
    for i in range(len(num_list)):
        if num_list[i]<0:
            num=i
            break
    return num