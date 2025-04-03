def solution(arr):
    new=[]
    for i in range(len(arr)):
        for j in range(arr[i]):
            new.append(arr[i])
    
    return new