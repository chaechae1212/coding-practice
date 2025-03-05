def solution(s):
    som=0
    s2=s.split() 
    newlist=[]
    for i in range(len(s2)):
        if s2[i]=='Z':
            som-=int(s2[i-1])
        else:
            som+=int(s2[i])
    return som