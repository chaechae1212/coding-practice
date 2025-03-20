def solution(array):
    
    my_list=[] 
    real_list=[] 
    check =[]
    for i in array:
        if i not in check:
            num=array.count(i)
            real_list.append(i);
            my_list.append(num);
            check.append(i)
    
    
    big=max(my_list)
    if my_list.count(big)>1:
        return -1;
        
    dex =my_list.index(big)
    result=real_list[dex]
        
    return result
                