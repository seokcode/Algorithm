def solution(n):
    return list(reversed([int(i) for i in str(n)]))

n = 12345
solution(n)

# return = [5,4,3,2,1]