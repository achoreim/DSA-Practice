"""
Easy
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/description/

Time to Solve: 6:37
"""


"""
Problem Description:

14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
4.3M
Submissions

"""


"""
My First Solution:

This is the most optimal solution according to LeetCode

"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize the return string
        ret_string = strs[0]

        # Initialize the count of characters in the return string
        count = 0

        for x in strs[1:]:
            for y in range(0, len(min(x, ret_string))):
                if x[y] == ret_string[y]:
                    count += 1
                else:
                    # break out of loop if a character is a mismatch
                    # This avoids going through the rest of a string
                    # that may have other matching characters
                    break

            # Set new Return String
            ret_string = x[0:count]
            # Reset count
            count = 0

        return ret_string
    
"""
Notes:

Mistakes I made:
    - in the second for loop: (for y in range(0, len(min(x, ret_string))):)
        I was originally getting an index out of bounds exception because some strings
        are larger than others. So I used the min() to find the shorter string.

What to Work on:
    - Check for any indexOutOfBounds errors when writing a for loop

"""