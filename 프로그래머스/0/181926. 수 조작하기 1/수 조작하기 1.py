def solution(n, control):
    sum=n
    for i in range(len(control)):
        if control[i]=="w":
            sum+=1
        elif control[i]=="s":
            sum-=1
        elif control[i]=="d":
            sum+=10
        elif control[i]=="a":
            sum-=10
    return sum