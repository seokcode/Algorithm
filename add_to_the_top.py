def n_sum(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    return sum


def n_sum2(n):
    result = n * (n + 1) // 2
    return result


# 재귀함수
def n_sum3(n):
    if n <= 1:
        return 1
    return n + n_sum3(n - 1)
