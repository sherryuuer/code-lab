# from 19
def get_median(nums):
    nums_sorted = sorted(nums)
    # print(nums_sorted)
    middle = len(nums_sorted) // 2
    if len(nums_sorted) % 2 == 0:
        low = middle - 1
        high = middle
        return (nums_sorted[low] + nums_sorted[high]) / 2
    return nums_sorted[middle]


nums = [3, 5, 2, 9, 4, 56, 3, 6]
res = get_median(nums)
print(res)
