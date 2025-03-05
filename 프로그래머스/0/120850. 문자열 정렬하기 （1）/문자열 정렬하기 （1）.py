def solution(my_string):
    my_list=[]
    my_string=list(my_string)
    for n in my_string:
        if n.isnumeric():
            my_list.append(int(n))
    my_list.sort()
    return my_list