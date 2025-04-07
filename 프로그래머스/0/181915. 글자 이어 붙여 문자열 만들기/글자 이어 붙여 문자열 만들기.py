def solution(my_string, index_list):
    new=""
    for i in range(len(index_list)):
        new+= my_string[index_list[i]]
        
    return new