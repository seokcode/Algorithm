arr1 = [[1,2,3,4]]
arr2 = [[3,2,3,4]]

result = [[0]*len(arr1[0]) for _ in range(len(arr1))]


for i in range(len(arr1)):
    for j in range(len(arr2[0])):
        result[i][j] = arr1[i][j] + arr2[i][j]
        print(result)
