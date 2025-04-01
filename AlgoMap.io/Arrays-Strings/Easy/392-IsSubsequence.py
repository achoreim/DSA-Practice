"""
Easy
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/description/

Time to solve: 4:52
"""


"""
Problem Description:

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you
want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""

"""
My First Solution:
Uses string Slicing => This is very space inefficient as python uses immutable strings. 
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        while len(t) is not 0:

            if len(s) is 0:
                break
            
            if s[0] == t[0]:
                s = s[1:]

            t = t[1:]

        if len(s) is 0:
            return True
        else:
            return False
        

"""
AI answer to the problem:

Uses a pure two-pointer solution, and is more space efficient compared to my solution.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # pointer for s
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)


        
"""

Solution Description:
    - Iterate through the t string and if you run into a char that matches with the s string, move to the
    next s character. Do this until you have iterated through the entire t string. Then if you have seen
    all s string characters, return True, otherwise return False.

Notes:
    - My solution is correct and works in O(n), but slicing strings repeatedly can be inefficient.
    A cleaner way is to use two pointers without slicing.

"""