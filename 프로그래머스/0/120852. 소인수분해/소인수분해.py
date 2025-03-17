def solution(n):
    my=[]
    i=2
    while n>1:
        if n%i==0:
            if i not in my:
                my.append(i)
            n//=i
        else:
            i+=1
    return sorted(my)

