"""
Easy
1. Two Sum
https://leetcode.com/problems/two-sum/description/

Time for first solution: 13:08
Time to compile all solutions and notes: 35:56
"""

"""
Problem Description:

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less
than O(n2) time complexity?
"""

"""
My First Solution: Involves index slicing and the use of .index()
This is a slow solution as .index() is a O(n) operation and is called many times

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = Counter(nums)

        for x in nums:
            if (target-x) in s:
                if (target-x == x):
                    if s[target-x] > 1:
                        return (nums.index(x), nums[nums.index(x)+1:].index(target-x) + nums.index(x) +  1)
                else:
                    return (nums.index(x), nums.index(target-x))
        
        return -1
    
"""
My Second Solution: (After learning the algorithm to use a seen{} hashmap)

Time Complexity: O(n)
Space COmplexity: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                return (seen[target-num], i)
            seen[num] = i
        
        return -1
    
"""
Notes:

    * What I learned: 
        - .index() is a O(n) operation, which makes multiple calls very slow
        - The enumerate for loop also keeps track of the index: "for i, num in enumerate(nums):"

    * What I can Improve on:
        - Use the enumerate for loop when you need the index: "for i, num in enumerate(nums):"
"""