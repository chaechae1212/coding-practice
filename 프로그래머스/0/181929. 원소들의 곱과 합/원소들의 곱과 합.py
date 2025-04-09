def solution(num_list):
    sum1=1
    sum2=0
    
    for i in range(len(num_list)):
        sum1*=num_list[i]
        sum2+=num_list[i]
        
    sum2=sum2**2
    if sum1<sum2:
        return 1
    else:
        return 0