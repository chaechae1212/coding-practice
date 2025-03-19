def solution(n):
    age=0
    for i in range(n):
        age+=1
        while age%3==0 or "3" in str(age):
            age+=1
       
    return age