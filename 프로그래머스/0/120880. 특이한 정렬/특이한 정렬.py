def solution(numlist, n):
    numlist=sorted(numlist,reverse=True)

    i=0
    new_list=[]
    while len(numlist)!=0:
        minn = float('inf')
        remember=0
        for i in range(len(numlist)):
            diff = abs(n - numlist[i])
            if diff < minn or (diff == minn and numlist[i] > numlist[remember]):  
                minn = diff
                remember = i
            
                
        new_list.append(numlist.pop(remember))
    return new_list
        
            