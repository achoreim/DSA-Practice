"""
Easy
344. Reverse String
https://leetcode.com/problems/reverse-string/description/

Time for first solution: 2:02
Time to compile all solutions and notes:
"""

"""
Problem Description:

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

"""

"""
My First Solution: Utilizing a two pointer solution
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left <= right:

            temp = s[right]

            s[right] = s[left]
            s[left] = temp

            left += 1
            right -= 1   

"""
My second solution:
Same time and space complexity as the first solution. However it is cleaner
because we have implemented tuple unpacking. This removes the need for a 'temp' variable
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left <= right:

            s[left], s[right] = s[right], s[left]
            
            left += 1
            right -= 1

"""
Notes:

    * What I have Learned:
        - There are different variations for two-pointer solutions, especially when dealing with
        incremental and decremental variations. In this problem we are guarranteed to do both
        to the left and right variable, however sometimes we can only increment or decrement
        when a condition is met.

    * What I can improve on:
        - This problem went by very smoothly, if anything maybe include some comments in the code
        as you solve the problem.
"""

             