def solution(n):
    sum1=0
    
    if n%2!=0:

        for i in range(1,n+1):
            if i%2!=0:
                sum1+=i
    
            
    
    if n%2==0:
        for i in range(2,n+1):
            if i%2==0:
                sum1=sum1+(i**2)
    return sum1
    
            