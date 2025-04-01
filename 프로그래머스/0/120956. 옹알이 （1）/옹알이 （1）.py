def solution(babbling):
    count=0;
    answer=""
    my=["aya", "ye", "woo", "ma"]
    for ba in babbling:
        for i in range(len(ba)):
            answer+=ba[i]
            if(answer in my):
                answer=""
        if answer=="":
            count+=1
        answer=""
    return count
		