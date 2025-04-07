def solution(numlog):
    
    result=""
    num=numlog[0]
    for i in range(1,len(numlog)):
        
        if num+1==numlog[i]:
            result+="w"
            num=num+1
        elif num-1==numlog[i]:
            result+="s"
            num-=1
        elif num+10==numlog[i]:
            result+="d"
            num+=10
        elif num-10==numlog[i]:
            result+="a"
            num-=10
       
    return result