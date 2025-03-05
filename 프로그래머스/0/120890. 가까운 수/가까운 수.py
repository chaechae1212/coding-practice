def solution(array, n):
    mii=100
    remember=0
    for i in range(len(array)):
        if abs(n-array[i])<mii:
            mii=abs(n-array[i])
            remember=i
        elif abs(n-array[i])==mii and array[i]<array[remember]:
            remember=i
    return array[remember]
            
        
