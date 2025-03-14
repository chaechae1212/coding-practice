def solution(num_list, n):
    m=[]
    r=[]
    for i in range(1,len(num_list)+1):
        if i%n==0:
            m.append(num_list[i-1])
            r.append(m)
            m=[]
        elif i%n!=0:
            m.append(num_list[i-1]) 
    return r