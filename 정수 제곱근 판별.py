import math
def solution(n):
    answer = math.sqrt(n)
    if answer != int(answer):
        return -1
    return pow(answer+1, 2)


n1 = 121
solution(n1)
# return 144

n2 = 3
solution(n2)
# -1