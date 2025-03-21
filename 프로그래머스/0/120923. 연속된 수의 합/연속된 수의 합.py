def solution(num, total):
    sum=0
    my=[]
    for i in range(0,num):
        sum+=i
    n=(total-sum)
    x=n/num
    for j in range(num):
        my.append(x)
        x+=1
    return my