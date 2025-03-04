def solution(hp):
    count=hp//5
    second=hp%5
    count+=second//3
    third = second%3
    count+= third//1
    return count