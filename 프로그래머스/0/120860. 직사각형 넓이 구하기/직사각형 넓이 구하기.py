def solution(dots):
    my=[]
    my2=[]
    for dot in dots:
        my.append(dot[0])
        my2.append(dot[1])
    
    x2=max(my)
    x=min(my)
    
    y2=max(my2)
    y=min(my2)
    
    return (x2-x)*(y2-y)