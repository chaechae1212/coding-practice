def solution(keyinput, board):
    count=0
    count2=0
    one=(board[0]-1)//2
    two=(board[1]-1)//2
    for i in range(len(keyinput)):
        if keyinput[i]=="left":
                count-=1
                if count<-one:
                    count=-one
                    
                    
        elif keyinput[i]=="right":
                 count+=1
                 if count>one:
                    count=one
        
        elif keyinput[i]=="down":
                count2-=1
                if count2<-two:
                    count2=-two
        elif keyinput[i]=="up":
                count2+=1
                if count2>two:
                    count2=two
   
    answer = [count,count2]
    return answer
    

          
