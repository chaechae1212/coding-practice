def solution(lines):
    first=[]
    second=[]
    third=[]
    nw=[]
    for i in range(lines[0][0],lines[0][1]):
            first.append(i)
    for i in range(lines[1][0],lines[1][1]):
            second.append(i)
    for i in range(lines[2][0],lines[2][1]):
            third.append(i)
            
    result=[]
    for i in first:
        if i in second and i not in result:
            result.append(i)
    for i in first:
        if i in third and i not in result:
            result.append(i)
    for i in second:
        if i in third and i not in result:
            result.append(i)
    answer=len(result)
    return answer
                
                
        