def solution(array):
    maxx=array[0]
    remeber=0
    mylist=[]
    for i in range(len(array)):
        if array[i]>maxx:
            maxx=array[i]
            remember = i
    mylist.append(maxx)
    mylist.append(remember)
    return mylist