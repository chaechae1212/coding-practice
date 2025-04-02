def solution(num_list):
    num_list=sorted(num_list)
    result=[]
    for i in range(5,len(num_list)):
        result.append(num_list[i])
    return result
