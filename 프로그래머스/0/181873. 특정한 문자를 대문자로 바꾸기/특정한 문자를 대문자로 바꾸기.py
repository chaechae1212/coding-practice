def solution(my_string, alp):
    result=""
    for i in range(len(my_string)):
        if my_string[i]==alp:
            result+=my_string[i].upper()
        else:
            result+=my_string[i]
    return result