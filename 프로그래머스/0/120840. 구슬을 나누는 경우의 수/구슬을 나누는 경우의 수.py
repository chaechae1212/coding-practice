def solution(balls, share):
    s=1
    m=1
    for i in range(balls,balls-share,-1):
        s*=i
    for j in range(1,share+1):
        m*=j
    return s//m
        