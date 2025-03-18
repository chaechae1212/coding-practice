
def solution(score):
    my=[]
    for sc in score:
        sc_avg=(sc[0]+sc[1])/2
        my.append(sc_avg)
    
    sorted_sco=sorted(my,reverse=True)
    ranks=[]
    
    for avg in my:
        rank=sorted_sco.index(avg)+1
        ranks.append(rank)
    return ranks
    