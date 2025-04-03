def solution(rny_string):
    result=""
    for i in range(0,len(rny_string)):
        if rny_string[i]=='m':
            result+='rn'
        else:
            result+=rny_string[i]
    return result