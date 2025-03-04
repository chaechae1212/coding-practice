def solution(order):
    count=0
    order=str(order)
    for i in range(len(order)):
        if order[i]=='3' or order[i]=='6' or order[i]=='9':
            count+=1
    return count
    