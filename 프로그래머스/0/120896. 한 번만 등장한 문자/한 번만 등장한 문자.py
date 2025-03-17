def solution(s):
    cot=0
    my=""
    for n in s:
        cot=s.count(n)
        if cot==1:
            my+=n
    my=sorted(my)
    return "".join(my)