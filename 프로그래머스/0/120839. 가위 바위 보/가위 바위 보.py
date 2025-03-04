def solution(rsp):
    result=""
    for n in rsp:
        if n=="2":
            result+="0"
        elif n=='0':
            result+="5"
        elif n=='5':
            result+="2"
            
    return result