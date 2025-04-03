def solution(myString):
    new=""
    result=[]
    for i in range(len(myString)):
        if myString[i]!='x':
             new+=myString[i]
        else:
            result.append(len(new))
            new=""
    result.append(len(new))
    return result