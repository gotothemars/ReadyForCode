# 归并排序

def merge_sort(nums):
    if len(nums) == 1:
        return nums

    mid = len(nums)//2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i = i + 1
        else:
            res.append(right[j])
            j = j + 1

    if i == len(left):
        while j < len(right):
            res.append(right[j])
            j = j + 1
    elif j == len(right):
        while i < len(left):
            res.append(left[i])
            i = i + 1

    return res

if __name__ == '__main__':
    nums = [5, 6, 3, 4, 2, 1]
    res = merge_sort(nums)
    print(res)