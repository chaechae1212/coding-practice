def solution(num, k):
    number=str(num)
    for i in range(0,len(number)):
         if str(k)==number[i]:
            return i+1
    return -1