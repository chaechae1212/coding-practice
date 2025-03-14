def solution(emergency):
    my=[0]*len(emergency)
    emergency_copy=emergency
    j=1
    for i in range(1,len(emergency)+1):
        a=max(emergency)
        dex=emergency_copy.index(a)
        my[dex]=j
        emergency_copy[dex]=-1
        j+=1
    return my
        