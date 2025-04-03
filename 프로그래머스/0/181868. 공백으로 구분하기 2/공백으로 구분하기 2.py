def solution(my_string):
    s_answer = ""
    b_answer=[]
    for i in range(len(my_string)):
        if my_string[i]!=" ":
            s_answer+=my_string[i]
        elif my_string[i]==" " and s_answer!="":
            b_answer.append(s_answer)
            s_answer=""
    if s_answer!="":
        b_answer.append(s_answer)
    return b_answer
            