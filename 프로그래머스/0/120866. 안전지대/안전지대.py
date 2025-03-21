def solution(board):
    point=[]
    box=[]
    j=0
    n=len(board[0])
    for b in board:
        for i in range(0,n):
                if b[i]==1:
                    point=[j,i]
                    box.append(point)
            
        j+=1
        
    for i in range(len(box)):
        row,col=box[i]
        board[row][col]=2
     
        if col-1>=0:
            board[row][col-1]=2
            
        if col+1<n:
            board[row][col+1]=2
            
        if row-1>=0:
            board[row-1][col]=2
            
        if row+1<n:
            board[row+1][col]=2
            
        if row-1>=0 and col-1>=0:
            board[row-1][col-1]=2
            
        if row-1>=0 and col+1<n:
            board[row-1][col+1]=2
            
        if row+1<n and col-1>=0:
            board[row+1][col-1]=2
            
        if row+1<n and col+1<n:
            board[row+1][col+1]=2
        
    total=0
    for row in board:
            total+=row.count(2)
    return n*n-total
     
    
                
                