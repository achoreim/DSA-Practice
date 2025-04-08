"""
Medium
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/description/

Time to solve: 22:45
"""

"""
Problem Description:

Given an integer array nums, return an array answer such that answer[i] is equal to
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)

"""


"""
My First Solution: (Brute Force)
Not Accepted: Time Limit Exceeded
"""

import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = nums.copy()
        sum = 1

        for x in range(0, len(nums)):
            newList = nums[:x] + nums[x+1:]
            sum = 1
            for y in newList:
                sum *= y
            output[x] = sum
        
        return output

"""
My second solution: (O(n) runtime) Coded after understanding the algorithm from Gregg Hog's
YouTube Video: https://www.youtube.com/watch?v=yKZFurr4GQA&ab_channel=GregHogg
"""

import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_list = nums.copy()
        right_list = nums.copy()
        output = nums.copy()

        multiplyer = 1

        for x in range(0, len(nums)):
            
            left_list[x] = multiplyer
            multiplyer *= nums[x]

        multiplyer = 1

        for i in range(len(nums) - 1, -1, -1):
            
            right_list[i] = multiplyer
            multiplyer *= nums[i]
        
        for j in range(0, len(nums)):
            output[j] = left_list[j] * right_list[j]

        return output
    

"""
Notes:

    How Can I Improve:
        - I was able to find the brute force solution to this problem, however, when it came to the
        optimal solution, I was not able to figure it out without help from Greg's video. This shows
        that I need more practice with these types of problems in order to figure out the patterns.

"""