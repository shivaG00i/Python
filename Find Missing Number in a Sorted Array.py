# 24. Find Missing Number in a Sorted Array Input: [1,2,3,5] → Output: 4


def find_missing_number(arr):
    n = len(arr)
    expected_sum = (n + 1) * (n + 2) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example usage
arr = [1, 2, 3, 5]
print(find_missing_number(arr))  # Output: 4




'''
Binary Search Approach (Faster for Large Arrays)
If the array is long, sorted, and only one number is missing, use binary search.

Code:
python
Copy
Edit
def find_missing_binary(nums):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        # Expected value at mid = nums[0] + mid
        if nums[mid] == nums[0] + mid:
            left = mid + 1
        else:
            right = mid - 1

    return nums[0] + left



'''