def solution(x):
    if x % sum([int(i) for i in str(x)]) == 0:
        return True
    return False


x1 = 10
x2 = 12
x3 = 11
x4 = 13

solution(x1)
# return = true
solution(x2)
# return = true
solution(x3)
# return = false
solution(x4)
# return = false
