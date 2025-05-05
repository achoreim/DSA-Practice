"""
Easy
83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Time for first solution: 16:07
Time to compile all solutions and notes: 
"""

"""
Problem Description:

Given the head of a sorted linked list, delete all duplicates such that
each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

"""
Initial Solution: 
Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        output = head
        cur = head.next
        head.next = None

        while head and cur:
            print(cur.val, head.val)

            if cur.val != head.val:
                print("Hit")
                head.next = cur
                head = head.next

            cur = cur.next
        
        if head:
            head.next = None
        
        return output
