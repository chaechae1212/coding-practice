def solution(num_list):
    x=0
    y=0
    for i in num_list:
         if i%2==0:
             x+=1
         else:
            y+=1
    list=[x,y]
    return list