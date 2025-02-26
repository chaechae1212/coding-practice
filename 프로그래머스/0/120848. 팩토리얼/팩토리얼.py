def solution(n):
    sum=1
    for i in range(1,n+1):
        sum*=i
        box=i
        if sum>n:
            return box-1
            break
    return i