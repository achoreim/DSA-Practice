"""
Easy
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/description/

Time for first solution: 6:06
Time to compile all solutions and notes: 18:26
"""

"""
Problem Description:

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []

"""

"""
My Initial Solution:
Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev

"""
Notes:

    * What I learned:
        - Startegy: Keeping a temp variable and iterate through the linkedlist with a while loop.

    * What I can work on:
        - Learn about dummy nodes.
"""


