import random


def qsort(nums):
    if len(nums) <= 1:
        return nums
    else:
        med = random.choice(nums)  # выбираем случайный элемент в списке nums
        before_nums = [x for x in nums if x < med]
        med_nums = [x for x in nums if x == med]
        after_nums = [x for x in nums if x > med]
        return qsort(before_nums) + med_nums + qsort(after_nums)


print(qsort([x * 2 for x in range(40, 2, -3)] + [x * 2 for x in range(40, 2, -3)]))
