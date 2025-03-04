def solution(n, numlist):
    mylist=[]
    for i in numlist:
        if i%n==0:
            mylist.append(i)
    return mylist
            