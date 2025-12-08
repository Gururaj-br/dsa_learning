'''
Problem Statement:
Write a function first_non_repeating(s) that takes a string and returns the first character that
does not repeat.
If all characters repeat, return None.
Input:
first_non_repeating("swiss")
first_non_repeating("aabbcc")
first_non_repeating("python")
Output:
w
None
p
'''

def first_non_repeating(s):
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    return None

# Test cases
print(first_non_repeating("swiss"))  # Output: w
print(first_non_repeating("aabbcc"))  # Output: None
print(first_non_repeating("python"))  # Output: p