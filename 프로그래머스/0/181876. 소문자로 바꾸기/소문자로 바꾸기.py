def solution(myString):
    result=""
    for i in range(len(myString)):
        result+=myString[i].lower()
    return result