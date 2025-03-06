def solution(a, b):
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            z=i
            
    a=a/z
    b=b/z
    
    while b!=1:
        if b%2!=0 and b%5!=0:
            return 2
            break
        if b%2==0:
            b=b/2
        if b%5==0:
            b=b/5
    
    return 1