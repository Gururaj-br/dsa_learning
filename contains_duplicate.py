'''
Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false


Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
'''

def hasDuplicate(self, nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example usage:
print(hasDuplicate([1, 2, 3, 3]))  # Output: True
print(hasDuplicate([1, 2, 3, 4]))  # Output: False
        

