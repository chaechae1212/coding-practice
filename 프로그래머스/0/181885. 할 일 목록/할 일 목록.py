def solution(todo_list, finished):
    new=[]
    for i in range(len(todo_list)):
        if not finished[i]:
            new.append(todo_list[i])
    return new