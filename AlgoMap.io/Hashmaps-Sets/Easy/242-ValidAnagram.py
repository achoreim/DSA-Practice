"""
Easy
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/

Time for first solution: 4:18
Time to compile all solutions and notes: 13:03
"""

"""
Problem Description:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters?
How would you adapt your solution to such a case?
"""

"""
My First Solution: Uses the Counter Class
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = Counter(s)
        t_dict = Counter(t)

        if s_dict == t_dict:
            return True
        
        return False
    
"""
Greg Hogg's Optimal Solution:
Very similar to my solution, however it is in a different order
"""

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict

# Let n be the length of the longest word
# Time complexity: O(n)
# Space complexity: O(n)

"""
Notes:
    
    * What I Learned:
        - The Counter class is a powerfill tool, and we can even use equivalence (==) on it.

    * What I can Improve on:
        - While attempting to solve the first soltution, I was using the set() class, while the
        correct solution was to use the counter() class. I kept running into edge cases before
        making the switch. If I took a little more time in the beginning to plan my solution, 
        this may have been avoided.
"""

