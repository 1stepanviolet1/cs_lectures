import random


def qsort(nums, left, right):
    if left >= right:
        return
    i, j = left, right
    med = random.choice(nums[left:right]) # выбираем случайный элемент в списке nums
    while i <= j:
        while nums[i] < med: i += 1
        while nums[j] > med: j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
        elif i == j:
            i, j = i + 1, j - 1
    qsort(nums, left, j)
    qsort(nums, i, right)
    return nums

nums = [x for x in range(30, -20, -3)] + [x * 2 for x in range(15, -1, -1)] + [x * 2 for x in range(2, 20, 2)]
print(qsort(nums, 0, len(nums)-1))
