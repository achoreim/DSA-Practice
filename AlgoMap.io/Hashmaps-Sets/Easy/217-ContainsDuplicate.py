"""
Easy
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/

Time to initially solve: 5:42
Time to compile all solutions and notes: 29:54
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
Inefficient, has a time complexity of: O(nlog(n)) due to the .sort() timesort method.
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
My second solution: Using sets as a data structure.

After getting the hint to use hash sets, the time it took to get this solution took 0:41 seconds.

Time Efficiency: 0()
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        s = set(nums)

        if len(nums) > len(s):
            return True

        return False
    
"""
Greg Hog's Solution:
This solution does some things similar to my second, such as creating a set. However it also includes
another loop that goes through the set while my solutin just compared the size of the lists.
"""

class Solution:
    def numJewelsInStones (self, jewels: str, stones: str) -> int:
        # O(n + m)
        s = set(jewels)
        count = 0
        for stone in stones:
            if stone in s:
                count += 1
        return count

# Time Complexity: O(n + m)
# Space Complexity: O(n)

"""
Notes:

    * What I learned:
        - The time complexity of calling the 'set()' constructor is O(n). (Yes it is a class, and we call the constructor)

    * What I can work on:
        - Read the error message: I spent a few minutes trying to get the sorted method to work, unbeknownst to me
        it was working, and I was running into a different compiler error seperate tot he sorted method.

        - Before starting to solve a problem, try to understand the different types of methods that I can use to solve
        it. In my first soltion, I tried to sort the list, but in my second solution, I used a hash set. The second
        solution was more optimal, and it would have been better to use that instead of waste my time with sorting.
    
"""