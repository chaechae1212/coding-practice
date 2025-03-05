def solution(numbers):
    my=""
    result=""
    mydic ={"one":1,"zero":0,"two":2,"three":3,
            "four":4, "five":5, "six":6, "seven":7,
            "eight":8,"nine":9}
    for i in numbers:
        my+=i
        if my in mydic:
              result+=str(mydic[my])
              my=""
    return int(result)