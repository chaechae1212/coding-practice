def solution(a, b):
    num=str(a)+str(b)
    result=int(num)
    if 2*a*b>result:
        return 2*a*b
    elif 2*a*b<result:
        return result
    elif 2*a*b==result:
        return result