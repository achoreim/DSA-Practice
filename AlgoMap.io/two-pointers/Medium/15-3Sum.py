"""
Medium
15. 3 Sum
https://leetcode.com/problems/3sum/description/

Time for first solution: 17:09 (solution not accepted)
Time to compile all solutions and notes:
"""

"""
Problem Description:

Given an integer array nums, return all the triplets [nums[i], nums[j],
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

"""
My First Solution: Solution was not accepted 
Time Complexity: O(n^2)
Space Complexity: O(n^2) => Because you are not checking for duplicates
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []

        for i in range(0, len(nums)-2):

            j = 0
            k = len(nums) -1
            print(nums[i])

            while j < k:
                print(nums[i], nums[j], nums[k])
                # Successfull triplet
                if (nums[i] + nums[j] + nums[k]) == 0:
                    if (i != j) and (i != k) and (j != k):
                        output.append([nums[i], nums[j], nums[k]])

                j += 1
                k -= 1
        
        return output

"""
Second Solution: Attempting to use a hashset:

After many failed attempts, I decided to revert to Greg Hogg's solutions,
and the following is from there:
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        h = {}
        n = len(nums)
        s = set()

        for i, num in enumerate(nums):
            h[num] = i

        for i in range(n):
            for j in range(i + 1, n):
                desired = -nums[i] - nums[j]
                if desired in h and h[desired] != i and h[desired] != j:
                    s.add(tuple(sorted([nums[i], nums[j], desired])))

        return list(s)
    
"""
Notes:

    * What I learned:
        - Match-switch in python is only after 3.10, other than that, it is better to use elifs
        - Sorting can be a powerfil tool, when you are doing two pointer solutions.

    * What I can work on:
        - Two Pointer solutions:
"""


        