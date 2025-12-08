'''
Valid Anagram
Solved 
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.


Recommended Time & Space Complexity
You should aim for a solution with O(n + m) time and O(1) space, where n is the length of the string s and m is the length of the string t.
'''

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return True if sorted(s) == sorted(t) else False
    
# Example usage:
print(isAnagram("racecar", "carrace"))  # Output: True
print(isAnagram("jar", "jam"))          # Output: False