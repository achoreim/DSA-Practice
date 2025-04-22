"""
Easy
169. Majority Element
https://leetcode.com/problems/majority-element/description/

Time for first solution:
Time to compile all solutions and notes:
"""

"""
Problem Description:

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋
times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""

"""
My first solution: O(n)
Time Complexity: O(n)
Space Complecity: O(n)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = Counter(nums)

        majority_element = num_count[0]
        majority_count = num_count[majority_element]

        for x in num_count:
            if num_count[x] > majority_count:
                majority_element = x
                majority_count = num_count[x]
        
        return majority_element