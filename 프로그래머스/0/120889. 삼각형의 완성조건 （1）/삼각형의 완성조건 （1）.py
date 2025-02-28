
def solution(sides):
    big=max(sides)
    sides.remove(big)
    if sides[0]+sides[1]>big:
        return 1
    else:
        return 2