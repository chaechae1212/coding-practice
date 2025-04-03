def solution(my_string, overwrite_string, s):
    j=0
    new=""
    for i in range(0,len(my_string)):
        if i>=s and j<len(overwrite_string):
            new+=overwrite_string[j]
            j+=1
        else:
            new+=my_string[i]
    return new