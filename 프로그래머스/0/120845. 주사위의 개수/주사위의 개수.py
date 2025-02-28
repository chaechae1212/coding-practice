def solution(box, n):
    sum=1
    for i in range(0,3):
         sum*=box[i]//n
    return sum