"""
Easy
682. Baseball Game
https://leetcode.com/problems/baseball-game/description/

Time for first solution: 16:12
Time to compile all solutions and notes: 26:15
"""

"""
Problem Description:

You are keeping the scores for a baseball game with strange rules.
At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the
ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the
operations.

The test cases are generated such that the answer and all intermediate
calculations fit in a 32-bit integer and that all operations are valid.

 

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
Example 3:

Input: ops = ["1","C"]
Output: 0
Explanation:
"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.
 

Constraints:

1 <= operations.length <= 1000
operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 104, 3 * 104].
For operation "+", there will always be at least two previous scores on the record.
For operations "C" and "D", there will always be at least one previous score on the record.
"""

"""
My initial soluiton:
Time Complexity: O(n) : Only one iteration throught the operations list
Space Complexity: O(n) : Only one list of extra space with a worst case scenario of n elements
"""

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []

        for x in operations:
            try:
                num = int(x)
                score_stack.append(num)
            except:
                if x == '+':
                    first_score = score_stack.pop()
                    second_score = score_stack[-1]
                    score_stack.append(first_score)
                    score_stack.append(int(first_score)+int(second_score))
                elif x == 'D':
                    prev_score = score_stack[-1]
                    score_stack.append(int(prev_score)*2)
                elif x == 'C':
                    score_stack.pop()

        total = 0

        for x in score_stack:
            total += int(x)
        
        return total

"""
Optimal Solution: Same time and space complexity, but cleaner and more readable code:
"""

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []

        for op in operations:
            if op == "+":
                stk.append(stk[-1] + stk[-2])
            elif op == "D":
                stk.append(stk[-1] * 2)
            elif op == "C":
                stk.pop()
            else:
                stk.append(int(op))

        return sum(stk)

"""
Notes: 

    * What I learned:
        - You can use some stack operations on a list in python
        - You can use a try-except block to see if a value is numeric (or a certain type)
          by forcing a type error 

    * What I can improve on:
        - Making my solutions cleaner: 
            - Using sum()
            - Not using a try-excpet block when there can be a work around
"""