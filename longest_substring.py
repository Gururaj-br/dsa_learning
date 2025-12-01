'''
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
Constraints:

0 <= s.length <= 1000
s may consist of printable ASCII characters.


Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(m) space, where n is the length of the string and m is the number of unique characters in the string.
'''

def longest_substring(s):
    seen = set()
    left = 0
    longest = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        longest = max(longest , len(seen))
    return longest

# Example usage:
print(longest_substring("zxyzxyz"))  # 3
print(longest_substring("xxxx"))      # 1