def solution(num_list, n):
    new=[]
    add=[]

    for i in range(len(num_list)):
        if i>=n:
            new.append(num_list[i])
        else:
            add.append(num_list[i])
    return new+add