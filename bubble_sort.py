input_list = [3, 2, 1, 5, 10, 2]
cnt = len(input_list)

for i in range(0, cnt, 1):
    for j in range(0, cnt-i-1, 1):
        if input_list[j] >= input_list[j+1]:
            temp = input_list[j]
            input_list[j] = input_list[j+1]
            input_list[j+1] = temp
print(input_list)

