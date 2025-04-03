def solution(arr1, arr2):
    count1=0
    count2=0
    if len(arr1)>len(arr2):
        return 1
    elif len(arr1)<len(arr2):
        return -1
    elif len(arr1)==len(arr2):
        for i in range(0,len(arr1)):
            count1+=arr1[i]
        for j in range(0,len(arr2)):
            count2+=arr2[j]
        if count1==count2:
            return 0
        elif count1>count2:
            return 1
        elif count2>count1:
            return -1
            