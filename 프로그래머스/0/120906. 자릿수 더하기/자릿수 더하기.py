def solution(n):
    mylist=list(str(n))
    sum=0
    for i in range(0,len(mylist)):
        sum+=int(mylist[i])
    return sum