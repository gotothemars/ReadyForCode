# leetcode 1109
# 差分数组
# 适用于频繁对原始数组的某个区间进行增减
# 如：nums[2:6] 全部加1， nums[3:9]全部减3
# 定义一个差分数组diff[]，使得diff[i] = nums[i] - nums[i-1]
# 可知：nums[i] = sum(diff[0..i])
# 因此：若在i以后的nums[i] 以后每一个加3，则只需要将diff[i]+3,因为之后的每个nums[]都会加上diff[i]
# 因此，将nums[i..j]上的每个加3，只需要将diff[i]+3,同时diff[j+1]-3

def getPlaneOrder(bookings, n):
    diff = [0 for i in range(n)]
    nums = [0 for i in range(n)]

    for booking in bookings:
        diff[booking[0] - 1] += booking[2]
        if booking[1] < n:
            diff[booking[1]] -= booking[2]

    nums[0] = diff[0]
    for i in range(1, n):
        nums[i] = nums[i - 1] + diff[i]

    return nums

if  __name__ == '__main__':
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    res = getPlaneOrder(bookings, n)
    print(res)