"""
Easy
169. Majority Element
https://leetcode.com/problems/majority-element/description/

Time for first solution O(n): 3:08 
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
My first solution: Uses the counter method and loops throgh it keeping track of the highest count
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
    
"""
My second solution: (After understanding the Boyer-Moore Voting Algorithm):
Time COmplexity; O(n)
Space Complexity: O(1)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for x in nums: 
            if count == 0:
                candidate = x
            if x == candidate:
                count +=1
            else:
                count -= 1

"""
Notes:

    * What I have learned:
        - Boyer-Moore Voting Algorithm: It is a neat algorithm when the contraints suggest that there is an
          element which apears 

    * What I can Improve on:
        - Figure out a way to loop without initializing the first elements to out of scope variables
          This strategy seems to be working for now, however I do not belive that it is the industry standard.

    * Miscelanious:
        - While attempting to solve this problem, I thought of a unique method that might  be great
          to write down: 
          If there was a way to sort the array in O(n) using counting sort, then we can probe 4 times at 25% intervals
          of the sorted array, since the majority element appears more than 50% of the time, it is guarranteed that
          two of the 4 probes would be the same number, and therefore the majority element.
          

"""