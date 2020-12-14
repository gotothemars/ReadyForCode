# 全排列求()的组合，注意点
# 1.global的使用
# 2.res.append(tmp[:])中 深拷贝的作用
# leetcode 22

def getalltarget(nums):
    global res
    if nums == 0:
        return []
    elif nums == 1:
        return ['()']
    else:
        res = []
        backtrace(nums, nums, '')
        return res

def backtrace(front, last, tmp):
    if front == 0:
        for i in range(last):
            tmp = tmp + ')'
        if tmp not in res:
            res.append(tmp[:])
        return

    if front < last:
        tmp = tmp + '('
        backtrace(front - 1, last, tmp)
        tmp = tmp[:-1] + ')'
        backtrace(front, last - 1, tmp)
    else:
        tmp = tmp + '('
        backtrace(front - 1, last, tmp)

if __name__ == '__main__':
    nums = 3
    res = getalltarget(nums)
    print(res)