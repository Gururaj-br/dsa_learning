
def find_min_rotated(nums):
    """
    Find minimum in rotated sorted array with distinct elements.
    Returns the minimum value.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# quick tests
# print(find_min_rotated([4,5,6,7,0,1,2]))  # -> 0
# print(find_min_rotated([3,4,5,1,2]))      # -> 1
# print(find_min_rotated([1]))   


nums = {2,3,4,5,6,1}
nums = list(nums)
left , right = 0, len(nums) - 1

while left < right:
    mid = (left + right) //2
    if nums[mid] > nums[right]:
        left = mid
    else:
        right = mid
print(nums[left])