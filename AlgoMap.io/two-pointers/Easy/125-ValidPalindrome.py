"""
Easy
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/description/

Time for first solution: 14:01
Time to compile all solutions and notes:
"""

"""
Problem Description:

A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include
letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


"""
My First Solution:
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Notes given from problem description:
        1. convert upper case to lower case
        2. Remove all non-alphanumeric characters
        3. .isalnum()
        """

        # Return true if s = ""
        if not s:
            return True

        left = 0
        right = len(s) - 1

        while left <= right:
            
            if s[left].isalnum() and s[right].isalnum():
                
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
            
            if left <= right:
                if not s[left].isalnum():
                    left += 1
                if not s[right].isalnum():
                    right -= 1

            

        return True
            
"""
My second solution:
The same as my first solution, but implementing the 'continue' keyword inside the while loop:
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        1. convert upper case to lower case
        2. Remove all non-alphanumeric characters
        3. .isalnum()
        """

        # Return true if s = ""
        if not s:
            return True

        left = 0
        right = len(s) - 1

        while left <= right:
            
            if s[left].isalnum() and s[right].isalnum():
                
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
                continue
            
            if not s[left].isalnum():
                left += 1
            if not s[right].isalnum():
                right -= 1

            

        return True


"""
Notes: 

    * What I Learned:
        - .isalnum() => A method that returns true or false if the given
                        character or string is alphanumeric or not.
        - If you use the 'continue' keyword inside a while loop, it will skip the rest of
          the while loop and restart another iteration.

    * What I can work on:
        - Iterating through the while loop: You need to make sure that you 
        are correctly incrementing and decrementing the left and right pointers correctly.

"""


