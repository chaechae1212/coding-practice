def solution(n):
    my=[n]
    while n!=1:
        if n%2==0:
            n=n//2
            my.append(n)
        else:
            n=3*n+1
            my.append(n)
    return my
            