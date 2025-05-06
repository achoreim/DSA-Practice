"""
Easy
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/description/

Time for first solution: 8:24 (With help from the solution)
Time to compile all solutions and notes: 
"""

"""
Problem Description:

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made
by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 


"""

"""
My Initial Solution:
Time Complexity: O(n)
Space Complexity: O(1) => Not creating new nodes but linking together already created nodes
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        cur = d

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
            
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return d.next

"""
Notes:

    * What I have learned:
        - This: 
                cur.next = list1
                cur = cur.next
                list1 = list1.next
    
          is the same as:

                cur.next = list1
                cur = list1
                list1 = list1.next

          the difference is only in the variable names, I feel as if the first iteration was
          a better and more readable interpretation of the solution as the second implementation
          makes it seem as if the cur node is being overriden.

    * What I can work on:
        - More practice with manipulating LinkedLists, this will make the problems solving process
          a lot smoother.

"""