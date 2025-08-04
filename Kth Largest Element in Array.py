# 20. Kth Largest Element in Array
# Input: [3,2,1,5,6,4], k=2 → Output: 5

array = [3,2,1,5,6,4]
k=2

def kth_largest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]
print(kth_largest(array, k))

''''' 


import random

def quickselect(nums, k):
    if not nums:
        return None
    
    pivot = random.choice(nums)
    left = [x for x in nums if x > pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x < pivot]

    L = len(left)
    M = len(mid)
    
    if k <= L:
        return quickselect(left, k)
    elif k <= L + M:
        return pivot
    else:
        return quickselect(right, k - L - M)



'''