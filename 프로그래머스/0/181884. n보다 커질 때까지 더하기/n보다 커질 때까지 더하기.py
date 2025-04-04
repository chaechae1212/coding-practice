def solution(numbers, n):
    sum=0
    for i in range(len(numbers)):
        sum+=numbers[i]
        if(sum>n):
            break
    return sum