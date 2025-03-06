def solution(my_string):
    answe=""
    total=0
    for char in my_string:
        if char.isnumeric():
            answe+=char
        else:
            if answe:
                total+=int(answe)
                answe=""
    if answe:
        total+=int(answe)
    return total
            