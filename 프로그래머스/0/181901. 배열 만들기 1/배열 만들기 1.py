def solution(n, k):
    new=[]
    for i in range(1,n+1):
        if i%k==0:
            new.append(i)
    return new