"""
Medium
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Time for first solution: 12:44
Time to compile all solutions and notes: 31:34
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
        # Cur goes ahead like normal, and behind is n nodes behind
        # Return 


        # Edge Case for no List
        if not head:
            return head
        
        # Edge Case for list of one element and n == 1
        if n == 1 and not head.next:
            return head.next
        
        # Set node pointers
        cur = behind = head
        count = 0

        while cur:
            cur = cur.next
            if count > n:
                behind = behind.next
            count += 1

        # Edge Case if n is equal to size of LList
        if count == n:
            return head.next
        
        # Skip the n'th from the end element
        if behind and behind.next:
            behind.next = behind.next.next


        return head

"""
Optimal Solution: The same time and space complexity as my solution, but uses
                  dummy node and makes the code a lot more readable.
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy

        for _ in range(n + 1):
            ahead = ahead.next

        while ahead:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next

        return dummy.next
    
"""
Notes:

    * What I Learned:
        - It is pythonic convention to use underscore (_) instead of a common variable letter
          to specify a 'throw away' variable that you do not wish to be used in the future.
          This was done in the optimal solution.

    * What I can work on:
        - Learn the dummt node technique and its usecases, and implement it when applicable. 
        - For this problem, our solution, althtough correct, had many different if statements to 
          counteract the different edge cases. It would be a lot cleaner and more profssional to 
          implement said edge cases in your algorithm.
"""

