input_str = 'abcdefg'

def reverse_string(s):
    result = ''
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result
# Example usage:
print(reverse_string(input_str))  # Output: "gfedcba"

def reverse_str(s):
    s = list(s)
    left , right = 0, len(s)-1
    for i in range(len(s)):
        if left >= right:
            break
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)
# Example usage:
print(reverse_str(input_str))  # Output: "gfedcba"