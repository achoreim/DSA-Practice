"""
Medium
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Time for first solution: 12:44
Time to compile all solutions and notes: 
"""

"""
Problem Description:

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""

"""
My Initial Solution:
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers:
        #

        if not head:
            return head
        
        if n == 1 and not head.next:
            return head.next
        
        print("Made it")
        cur = behind = head
        count = 0

        while cur:
            cur = cur.next
            print(count, n)
            if count > n:
                behind = behind.next
            count += 1

        if count == n:
            return head.next
        
        if behind and behind.next:
            behind.next = behind.next.next

        return head
    


