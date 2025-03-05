def solution(sides):
    count=0
    big=max(sides[0],sides[1])
    sides.remove(big)
    for i in range(1,big):
        if big<sides[0]+i:
            count+=1
    for j in range(big,(sides[0]+big)):
         if j<sides[0]+big:
            count+=1
    return count