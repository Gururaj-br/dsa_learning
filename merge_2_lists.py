'''
merge two lists
Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
'''

def mergeTwoLists(list1, list2):
    merged = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j +=1
    
    if i < len(list1):
        merged.extend(list1[i:])
    if j < len(list2):
        merged.extend(list2[j:])

    return merged

# Example usage:
list1 = [1,2,4]
list2 = [1,3,5]
print(mergeTwoLists(list1, list2))  # Output: [1,1,2,3,4,5]

list1 = [1,2,34,56,78]
list2 = [2,3,5]
print(mergeTwoLists(list1, list2))  # Output: [1,2,2,3,5,34,56,78]