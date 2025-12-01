'''
Reverse Linked List
Solved 
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []
Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000


Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(1) space, where n is the length of the given list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def reverseList(self, head: ListNode):
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev to current
            current = next_node       # Move to the next node
            
        return prev
    
# Example usage:
# Creating a linked list 0 -> 1 -> 2 -> 3
head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
solution = Solution()
reversed_head = solution.reverseList(head)