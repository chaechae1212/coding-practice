def solution(num_list, n):
    new=[]
    for i in range(0,len(num_list),n):
        new.append(num_list[i])
    return new
        