def solution(my_string):
    list = ['a','e','i','o','u']
    answer = ''
    for i in my_string:
        if i not in list:
            answer += i

    return answer