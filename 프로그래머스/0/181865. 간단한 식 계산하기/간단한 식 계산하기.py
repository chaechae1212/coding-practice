def solution(binomial):
    new=[]

    new=binomial.split()
    sum=int(new[0])

    for i in range(1,len(new),2):
        if new[i]=="+":
            sum+=int(new[i+1])
        elif new[i]=="-":
            sum-=int(new[i+1])
        elif new[i]=="*":
            sum*=int(new[i+1])
    return sum