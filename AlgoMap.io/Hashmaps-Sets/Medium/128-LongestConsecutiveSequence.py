"""
Medium
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/

Time for first solution O(n): 14:51
Time to compile all solutions and notes:
"""

"""
Problem Description:

Given an unsorted array of integers nums, return the length
of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

"""
My First Soltution:
Time Complexity: O(nlog(n)) => Bottle necked by the sorted() method which runs at O(nlog(n))
Space Complexity: O(n)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        sorted_nums = sorted(nums)

        longest_count = 1
        current_count = 1
        prev = sorted_nums[0]

        for num in sorted_nums:
            if num == prev+1:
                current_count += 1
            elif num != prev:
                current_count = 1

            if current_count > longest_count:
                longest_count = current_count
            
            prev = num
        
        return longest_count


"""
AI Answer: Explains the O(n) space and time optimized solution.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # only start sequence if num is the beginning of one
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # walk forward through the consecutive sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
    

    
"""
Notes:

    * What I have learned:
        - When Counting a new sequence in an unsorted list: Make sure to only start counting when 
          an element n-1 does not exist, otherwise you will start counting in the middle of a sequence.

    * What I can improve on:
        - Always make sure to check for edge cases and invalid input, unless otherwise stated.
          In this problem we did not account for empty input.
"""