def solution(my_string, m, c):
    big=[]
    new=''
    result=''
    for i in range(0,len(my_string),m):
        for j in range(i,i+m):
            new+=my_string[j]
        big.append(new)
        new=''
    for st in big:
        result+=st[c-1]
    return result
        
    