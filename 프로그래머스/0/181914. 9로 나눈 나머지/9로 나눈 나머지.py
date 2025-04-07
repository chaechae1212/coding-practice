def solution(number):
    sum=0
    for i in range(len(number)):
        sum+=int(number[i])
 
    na=sum%9
    box=int(number)%9
    
    if box==na:
        return na