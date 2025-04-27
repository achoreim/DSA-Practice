"""
Easy
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/description/

Time for first solution: 3:33
Time to compile all solutions and notes: 37:11
"""

"""
Problem Description:

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is
very trivial, could you find an O(n) solution using a different approach?
"""

"""
My First Solution: Very trivial solution: 1. Iterate, 2. Square, 3. Sort
Time Complexity: O(nLog(n))
Space Complexity: O(1)
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Iterate through the array
        for i, num in enumerate(nums):
            # Square each element
            nums[i] = num * num

        # Sort the final array O(nLog(n))
        nums.sort()
        return nums


"""
Second Solution: Utilising a sliding window approach

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        return_list = []

        while left <= right:
            left_num = nums[left] ** 2
            right_num = nums[right] ** 2
            if left_num >= right_num:
                return_list.append(left_num)
                left += 1
            else:
                return_list.append(right_num)
                right -= 1
            
        return_list.reverse()

        return return_list

    
"""
Notes:

* What I have learned:
    - A two pointer python loop using the while loop: 

        left = 0
        right = len(nums) - 1

        while left <= right:
            # Do something with nums[left] and nums[right]

            if condition:
                left += 1
            else:
                right -= 1

* What I can work on:
    - Make sure that I read the prompt, there is valuable information in it. 
      For this problem a very big hint is that the "array nums sorted in non-decreasing order"

"""