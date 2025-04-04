def solution(my_string):
    result=""
    new=[]
    for i in range(len(my_string)):
        for j in range(i,len(my_string)):
            result+=my_string[j]
        new.append(result)
        result=""
    new=sorted(new)
    return new