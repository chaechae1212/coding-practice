def solution(my_string, is_suffix):
    new=[]
    num=0
    for i in range(len(my_string)-1,-1,-1):
        new.insert(0,my_string[i])
        if new==list(is_suffix):
            num=1
            break
    return num