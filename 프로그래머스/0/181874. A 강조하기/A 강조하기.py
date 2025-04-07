def solution(myString):
    result=""
    for i in range(len(myString)):
        if myString[i]=='a':
            result+=myString[i].upper()
        elif myString[i]!='A':
            result+=myString[i].lower()
        else:
            result+=myString[i]
    return result