def solution(arr):
    new=[]
    for i in range(len(arr)):
        if arr[i]>=50 and arr[i]%2==0:
            new.append(arr[i]//2)
        elif arr[i]<50 and arr[i]%2!=0:
            new.append(arr[i]*2)
        else:
            new.append(arr[i])
    return new