def solution(my_string, is_prefix):
    num=0
    result=""
    for i in range(len(my_string)):
        result+=my_string[i]
        if result==is_prefix:
            num=1
            break
    return num