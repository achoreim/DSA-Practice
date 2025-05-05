"""
Easy
83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Time for first solution: 16:07
Time to compile all solutions and notes: 27:43
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

            if cur.val != head.val:
                head.next = cur
                head = head.next

            cur = cur.next
        
        if head:
            head.next = None
        
        return output


"""
Optimal Solution: This solution has the same time complexity as mine, but is more readable
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
    
"""
Notes:

    * What I learned:
        - It would be more consise to keep head as it is and use that as the return value, while
          altering 'cur' a temp variable used to iterate through the list.

    * What I can work on:
        - I feel very rusty when it comes to linkedlists problems, I remember being able to 
          flash through them, as they were my favorite type of problem to solve, I know that
          I just need more practice through repititon in order ot be able to go back to feeling
          comfortable with them again.
        - Be more precised and think of a way to satisfy each and every edge case with one implementation
          as you can see, in my comde there are multiple if statements each satisfying a differnte edge case
          when with a little more thinking, they could have been solved like how the optimal solution does it.
"""