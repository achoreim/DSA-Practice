"""
Easy
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Time to solve: 22:45
"""


"""
Problem Description:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However,
the numeral for four is not IIII. Instead, the number four is written as IV. Because the
one is before the five we subtract it making four. The same principle applies to the number
nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

"""


"""
My 1st Solution:

Time complexity: O(n)
"""


class Solution:
    def romanToInt(self, s: str) -> int:

        # Create a dict for roman to numerical conversions
        romanDict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000, 
        }

        # initialize sum to 0
        sum = 0

        # keep track of previous roman numeral
        lastRoman = s[0]

        # loop through roman numeral string
        for x in s:
            # if current numeral is greater than the last one then subtract
            if romanDict[x] > romanDict[lastRoman]:
                sum -= romanDict[lastRoman]
                sum += (romanDict[x]-romanDict[lastRoman])
            # add new roman numeral to sum
            else:
                sum += romanDict[x]

            # update last roman numeral
            lastRoman = x

        # return result
        return sum


"""
Mistakes I made:
    - Not understanding the intracisies of roman numerals before attempting to solve the problem.
        - I didnt know that there could only be one smaller numeral before a larger one, which caused
          me to go about solving the problem in a different way.
    - Not necessarily a mistake, but I added the previous numeral before checking if it should have
      been subtracted — this caused me to add, then subtract, instead of just handling the subtractive
      case directly.


      


Notes: 
    - This problem was a great example of why test cases and their outputs should be understood before
      diving in to solve the problem. You can save yourself a lot of time and confusion by doing so.
"""