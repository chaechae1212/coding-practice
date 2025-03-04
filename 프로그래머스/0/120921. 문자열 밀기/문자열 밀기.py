def solution(A, B):
    for i in range(1,len(A)):
        if A==B:
            return 0
        my=A[-i:]+A[:-i]
        if my==B:
                return i

    return -1
        