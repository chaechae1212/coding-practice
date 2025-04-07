def solution(my_strings, parts):
    new=""
    for i in range(len(my_strings)):
        for j in range(parts[i][0],parts[i][1]+1):
            new+=my_strings[i][j]
    return new