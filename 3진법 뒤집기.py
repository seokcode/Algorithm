def solution(n):
    trans = ''
    while n:
        trans += str(n % 3)
        print(trans)
        n = n // 3
    return int(trans, 3)


n1 = 45
n2 = 125

solution(n1)
#return (10진법) (3진법) 앞뒤 반전(3진법) 10진법으로 표현
#         45	 1200	   0021	         7
solution(n2)
#return (10진법) (3진법) 앞뒤 반전(3진법) 10진법으로 표현
#         125	 11122	   22111	    229