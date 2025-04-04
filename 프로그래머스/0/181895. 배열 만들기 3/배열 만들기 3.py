def solution(arr, intervals):
    first=[]
    second=[]
    for i in range(len(arr)):
            if i>=intervals[0][0] and i<=intervals[0][1]:
                first.append(arr[i])
    for i in range(len(arr)):
            if i>=intervals[1][0] and i<=intervals[1][1]:
                second.append(arr[i])
    return first+second
            
      