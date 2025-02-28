def solution(n):
    result=n//7
    if n%7!=0:
        return result+1
    else:
        return result