'''
Binary Search
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in 
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.


Recommended Time & Space Complexity
You should aim for a solution with O(logn) time and O(1) space, where n is the size of the input array.
'''

def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid +1
        else:
            return mid
    return -1

#example 
print(search([-1,0,2,4,6,8], 4))  # 3
print(search([-1,0,2,4,6,8], 3)) # -1