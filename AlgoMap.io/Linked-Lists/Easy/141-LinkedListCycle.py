"""
Easy
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/description/

Time for first solution: DNF
Time to compile all solutions and notes:
"""

"""
Problem Description:

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer. Internally, pos is used to
denote the index of the node that tail's next pointer is connected to. Note that pos is
not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

"""
My Inital Solution: Utilizing a set to come accross repeat values


This is incorrect because the linkedlista are not contrained to not contain duplicate values
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()

        while head:
            if head.val in s:
                return True
            else:
                s.add(head.val)
            head = head.next
        
        return False
    
"""
Optimal Solution:
Time Complexity: O(n) just iterating through the linkedlist
Space COmpelxity: O(1) => No extra space was used
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
            
        
        return False
    
"""
Notes:

    *What I have learned:
        - Floyd’s Cycle Detection Algorithm (also called the “tortoise and hare” algorithm)

    *What I can Work on:
        - Learning more nifty and useful algorithms such as the Floyd’s Cycle Detection
        Algorithm (also called the “tortoise and hare” algorithm)

    
"""