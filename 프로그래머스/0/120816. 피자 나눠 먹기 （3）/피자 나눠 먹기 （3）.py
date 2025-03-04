def solution(slice, n):
    result=n//slice
    if n%slice!=0:
        result+=1
    return result