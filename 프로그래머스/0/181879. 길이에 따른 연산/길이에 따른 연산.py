def solution(num_list):
    
    gop=1
    if(len(num_list)>=11):
        gop-=1
        for i in range(0,len(num_list)):
            gop+=num_list[i]
    else:
         for i in range(0,len(num_list)):
                gop*=num_list[i]
    return gop