def solution(before, after):
    new_b=sorted(before)
    new_a=sorted(after)
    if new_b==new_a:
        return 1
    else:
        return 0 