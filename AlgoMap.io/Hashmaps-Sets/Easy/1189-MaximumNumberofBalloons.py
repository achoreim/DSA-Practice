"""
Easy
1189. Maximum Number of Balloons
https://leetcode.com/problems/maximum-number-of-balloons/description/

Time for first solution:
Time to compile all solutions and notes:
"""

"""
Problem Description:

Given a string text, you want to use the characters of text
to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the
maximum number of instances that can be formed.

 

Example 1:

Input: text = "nlaebolko"
Output: 1
Example 2:


Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
 

Note: This question is the same as 2287: Rearrange Characters to Make Target String.
"""

"""
My First Solution: Using the set() class

Solution not accpeted: Fails the text case of "balon"
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count = 0

        b_set = set("balloon")

        text_set = set()

        empty_set = set()

        for x in text:
            if x in b_set:
                text_set.add(x)
            if text_set == b_set:
                count += 1
                text_set.clear()

        return count


"""
My Second Solution: Using the Counter() class
Time Complexity:
Space Complexity:
"""
