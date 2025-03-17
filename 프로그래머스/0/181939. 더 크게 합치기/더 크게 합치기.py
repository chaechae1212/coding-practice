def solution(a, b):
    one=str(a)+str(b)
    two=str(b)+str(a)
    
    if int(one)<int(two):
        return int(two)
    elif int(one)>int(two) or int(one)==int(two):
        return int(one)