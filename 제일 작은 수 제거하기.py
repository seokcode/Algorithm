def solution(arr):
    min_arr = arr.index(min(arr))
    arr.pop(min_arr)
    if not arr:
        return [-1]
    return arr


arr1 = [4,3,2,1]
solution(arr1)
# return [4,3,2]

arr2 = [10]
solution(arr2)
# return [-1]