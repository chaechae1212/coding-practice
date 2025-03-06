def solution(quiz):
    my_list=[]
    z=0
    for letter in quiz:
        letter=letter.split(" ")
        if letter[1]=='-':
            z=int(letter[0])-int(letter[2])
        elif letter[1]=='+':
            z=int(letter[0])+int(letter[2])
        if z==int(letter[4]):
            my_list.append("O")
        elif z!=int(letter[4]):
            my_list.append("X")
    return my_list
            
            
            