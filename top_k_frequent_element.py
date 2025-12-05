def topKFrequent(nums, k):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    items = list(freq.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return [items[i][0] for i in range(k)]


# Example usage:
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
# Output: [1, 2]