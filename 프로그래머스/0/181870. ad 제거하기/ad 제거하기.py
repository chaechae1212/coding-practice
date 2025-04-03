def solution(strArr):
    result=[]
    for str in strArr:
        if "ad" not in str:
            result.append(str)
            
    return result