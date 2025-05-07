"""
Easy
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/description/

Time for first solution: 4:09
Time to compile all solutions and notes: 12:23
"""

"""
Problem Description:

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

"""
My Initial Solution: 
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
"""
Notes:

    *What I have Learned:
        - The fast vs slow pointer can also be useful on no cycle related questions as well
        - When it comes to the while loop, since the fast pointer is skipping by two nodes at once, 
          make sure to always includ it in the check as: 
                '''
                    while fast and fast.next:
                '''
          because if you do this:
                '''
                    while slow and fast.next:
                '''
          you will run ito a Nonetype exception

    *What I can work on:
        - Make sure that I read the input output examples correctly before starting to solve a problem
          this mistake made me lose the curical initial few minutes of the problem solving process.
"""