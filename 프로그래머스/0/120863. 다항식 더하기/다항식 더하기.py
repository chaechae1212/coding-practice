def solution(polynomial):
    my=polynomial.split("+")
    new=[]
    s=0
    s_2=0
    for m in my:
        m=m.strip()
        if "x" in m:
            if m=="x": 
                s+=1 
                
            else:
                s+=int(m[:-1]) 
                    
        else:
            s_2+=int(m)
    if s>0:
        if s>1:
            new.append(f"{s}x")
        else:
            new.append("x")
    if s_2>0:
        new.append(str(s_2))
    return " + ".join(new)
  
            