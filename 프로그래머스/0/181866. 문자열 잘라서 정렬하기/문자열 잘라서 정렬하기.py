def solution(myString):
    big=[]
    small=''
    for i in range(len(myString)):
        if myString[i]!='x':
            small+=myString[i]
        if myString[i]=='x':
            if small!='':
                big.append(small)
                small=''
    if small!='':
        big.append(small)
    return sorted(big)