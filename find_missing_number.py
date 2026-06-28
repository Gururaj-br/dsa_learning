"""to find missing number in an array of size n containing numbers from 0 to n."""

arr = [0, 1, 2, 3, 5]  # Example array with a missing number

def find_missing_number(arr):
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

def find_missing_with_set(arr):
    num_set = set(arr)
    n = len(arr)
    for i in range(n + 1):
        if i not in num_set:
            return i

# print(find_missing(arr))  # Output: 4
print(find_missing_with_set(arr))
