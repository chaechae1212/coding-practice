def solution(my_string):
    answer = ""
    new=[]
    for i in range(len(my_string)):
        if my_string[i]!=" ":
            answer+=my_string[i]
        elif my_string[i]==" ":
            new.append(answer)
            answer=""
    if answer!="":
        new.append(answer)
    return new