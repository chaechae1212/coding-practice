def solution(my_String):
    new=""
    for i in range(len(my_String)):
        if my_String[i]<'l':
            new+='l'
        else:
            new+=my_String[i]
    return new