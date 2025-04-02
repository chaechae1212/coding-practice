def solution(n_str):
    answer=""
    for i in range(len(n_str)):
        if n_str[i]!='0':
            remeber =i
            break
    for j in range(i,len(n_str)):
        answer+=n_str[j]
    return answer
        
            
    