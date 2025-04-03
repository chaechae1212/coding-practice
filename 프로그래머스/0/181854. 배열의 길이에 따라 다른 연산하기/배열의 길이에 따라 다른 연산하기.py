def solution(arr, n):
    if len(arr)%2==0:
        for i in range(1,len(arr),2):
             arr[i]=arr[i]+n
    else:
        for j in range(0,len(arr),2):
            arr[j]=arr[j]+n
    return arr