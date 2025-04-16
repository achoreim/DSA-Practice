"""
Easy
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/

Time to solve: 5:42
"""

"""
Problem Description:

Given an integer array nums, return true if any value appears at
least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

"""
My First Solution:
Inefficnet, has a time complexity of: O(nlog(n)) due to the .sort() timesort method.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Sort the list
        nums.sort()
        
        # Iterate through the list.
        for x in range(0, len(nums)):
            if x > 0:
                # Return false if last element is the same
                if nums[x-1] == nums[x]:
                    return True

        return False

"""
Notes:

    * What I can work on:
        - Read the error message: I spent a few minutes trying to get the sorted method to work, unbeknownst to me
        it was working, and I was running into a different compiler error seperate tot he sorted method.
    
"""