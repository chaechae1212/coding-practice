def solution(M, N):
    m=max(M,N)
    s=min(M,N)
    count=m-1
    count+=(s-1)*m
    return count