def solution(n):
    for i in range(max(6,n),(6*n)+1):
        if i%6==0 and i%n==0:
            result=i//6
            break
    return result