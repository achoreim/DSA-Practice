"""
Medium
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Time for first solution (Brute Force O(n^2) not accepted:): 6:01
Time to compile all solutions and notes: 26:41
"""

"""
Problem Description:

Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an
integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not
use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""


"""
My First Solution: Brute Force O(n^2) solution:

Time Complexity: O(n^2)
Space Compelxity: O(1)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute Force O(n^2) Solution:

        for i in range(0, len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        
        return -1
    
"""
My second solution: Utilizing the two pointer solution:
Time Compelxity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l <= r:
            lnum = numbers[l]
            rnum = numbers[r]
            if lnum+rnum == target:
                return [l+1, r+1]
            else:
                if lnum+rnum > target:
                    r -= 1
                if lnum+rnum < target:
                    l += 1
        
        return -1



"""
Notes:

* What I have learned:
    - Whenever the input array is sorted in non decreseing order or any order as a matter of fact,
    and is explicitly mentioned in the problem description, make sure to understand that that could
    be a useful tip when solving the problem. 
    - It is also very useful to visualise the problem, in this problem we understood that we needed
    to use a two pointer solutionl however the solution was not apparent until a visualasation was seen.

* What I can Improve on:
    - When using a two pointer solution, make sure to understand when to use indices and when to 
    reference the element of the array. In this problem I made a mistake when 
    - Make the code cleaner, there is no need for lnum and rnum, when you could have just used
     a sigular 'total' as a variable for the addition of both positions.
"""


        