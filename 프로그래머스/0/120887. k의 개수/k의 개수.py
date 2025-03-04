def solution(i, j, k):
    count=0
    for n in range(i,j+1):
        count+=str(n).count(str(k))
    return count
            