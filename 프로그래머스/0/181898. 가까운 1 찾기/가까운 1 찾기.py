def solution(arr, idx):
    
    num=-1
    for i in range(len(arr)):
        if idx<=i and arr[i]==1:
            num=i
            break
    return num