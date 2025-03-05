def solution(my_string):
    result=my_string.lower()
    result=list(result)
    result.sort()
    return ''.join(result)