"""
Easy
2239. Find Closest Number to Zero
https://leetcode.com/problems/find-closest-number-to-zero/description/
"""

"""
Problem Description: 

Given an integer array nums of size n, return the number with the value closest to 0 in
nums. If there are multiple answers, return the number with the largest value.

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
 

Constraints:

1 <= n <= 1000
-105 <= nums[i] <= 105

"""


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # closest variable to be returned, we initialize it as the first element in the list
        closest = nums[0]

        # Iterate through the list
        for x in nums:
            # If x is the same distance from 0 as closest, then closest must be the larger of the two
            if abs(x) == abs(closest):
                if x > closest:
                    closest = x
            # If the distance x is from 0 is smaller than closest, then we change the closest to 
            if abs(x) < abs(closest):
                closest = x
        
        # Exit the loop and return the closest element to 0
        return closest
    

"""
Solution:

    Time Complexity: The solution is in O(n) as we only interate through the list once. 

    We keep a variable named 'Closest' to keep track of the closest element, and update it
    throughout the loop if we find a more suitable element.




Notes:

This is the first problem that I have worked on in a while, even though it was easy. I had made many
rudementary problems with the python syntax, and basic boolean operations. I ran tests 3 times before
finding the correct solution.

"""
        