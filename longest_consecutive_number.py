'''
Longest Consecutive Sequence - Medium
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9


Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.
'''

class Solution:
    def longestConsecutive(self, nums: list[int]):
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            if n-1 not in nums_set:
                length = 1
                while n+length in nums_set:
                    length +=1
                longest = max(longest , length)

        return longest        
        
#example
solution = Solution()
print(solution.longestConsecutive([2,20,4,10,3,4,5]))
print(solution.longestConsecutive([0,3,2,5,4,6,1,1]))