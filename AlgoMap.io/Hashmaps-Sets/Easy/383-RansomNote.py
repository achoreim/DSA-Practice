"""
Easy
383. Ransom Note
https://leetcode.com/problems/ransom-note/description/

Time for first solution: 5:37
Time to compile all solutions and notes: 19:39
"""

"""
Problem Description:
Given two strings ransomNote and magazine, return true if
ransomNote can be constructed by using the letters from magazine
and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

"""
My first solution:
My solution involves first creating a dictionary, then iterating through the ransomNote
while decrementing from the dictionary. 

Time complexity: O(m+n)
Space Complexity: O(k) where k is = 26 if there are only lowercase letters allowed in the input ~ O(n)
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag_dict = {}

        for x in magazine:
            if x in mag_dict:
                mag_dict[x] += 1
            else:
                mag_dict[x] = 1


        for x in ransomNote:
            if (x in mag_dict) and (mag_dict[x] > 0):
                    mag_dict[x] -= 1
            else:
                return False

        return True


"""
Greg Hogg's Optimal Solution using counter:
"""

# Optimal Solution
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine) # TC for Counter is O(n)

        for ch in ransomNote:
            if hashmap[ch] > 0:
                hashmap[ch]-=1
            else:
                return False
        return True

# Time Complexity: O(R + M)  -> R = len(ransomNote), M = len(magazine)
# Space Complexity: O(M)     -> we're using a hashmap 


"""
Notes:

    * What I learned: 

        - Collections counter is a C built in loop, which is much faster than python loops. It
        is more efficient to use a counter than it is to use a python loop. Even though the time
        complexity is the same.



    * What I can Improve on:

        - Instead of making a loop to count the elements of a list into a dictionary, it is more
        convinient and time efficient to use the Counter class.
"""