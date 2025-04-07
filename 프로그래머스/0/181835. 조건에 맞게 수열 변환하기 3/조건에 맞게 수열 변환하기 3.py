def solution(arr, k):
    new=[]
    for i in range(len(arr)):
        if k%2!=0:
            new.append(arr[i]*k)
        else:
            new.append(arr[i]+k)
    return new