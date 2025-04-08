"""
Medium
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/description/

Time to solve: 
"""

"""
Problem Description:

Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping
intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


"""
My First Solution:

Was not Accepted: Incorrect => Failed first test
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        # Output: [[1,6],[8,10],[15,18]]

        output = []

        currBeg = intervals[0][0] #1
        prevLast = intervals[0][1] #4
        changeBeg = False

        for x in range(1, len(intervals)):
            interval = intervals[x]

            

            if changeBeg:
                currBeg = interval[0]

            print(currBeg)

            
            
            if interval[0] <= prevLast:
                # print(interval[0] , prevLast)
                changeBeg = False
                # Edge Case for Last interval
                if x == len(intervals)-1:
                    newInterval = [currBeg, interval[1]]
                    output.append(newInterval)
            else:
                # print(currBeg, interval[1])
                newInterval = [currBeg, interval[1]]
                output.append(newInterval)
                # Update CurrBeg:
                changeBeg = True
            
            prevLast = interval[1]
            
        return output
                
"""
AI Answer:

"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        output = []
        currBeg = intervals[0][0]
        prevLast = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start <= prevLast:
                # Overlapping — extend the previous interval
                prevLast = max(prevLast, end)
            else:
                # No overlap — push the current merged interval
                output.append([currBeg, prevLast])
                currBeg = start
                prevLast = end

        # Add the last interval
        output.append([currBeg, prevLast])

        return output


"""
My Own Answer After Watching Greg's Videp:

"""