def solution(myString, pat):
    new=""
    for i in range(len(myString)):
        if myString[i]=="A":
            new+='B'
        else:
            new+='A'
    if pat in new:
        return 1
    return 0