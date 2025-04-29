"""
Easy
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/

Time for first solution: 20:20
Time to compile all solutions and notes: 38:15
"""

"""
Problem Description:

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

"""
My initial solution:
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Two Stacks:
        #   S itself will be a stack
        #   Temp stack: Includes all open parentheses

        paren_dict = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        s_stack = list(s)
        open_stack = []

        while s_stack:
            top = s_stack.pop()
            if not open_stack:
                open_stack.append(top)
            elif top in paren_dict:
                if open_stack[-1] == paren_dict[top]:
                    open_stack.pop()
                else:
                    return False
            else:
                open_stack.append(top)


        if open_stack:
            return False
            
        return True
    
"""
Most optimal solution: 
The same time and space complexity as my solution, but this implemenation
uses only one stack, and is more readable:
"""

class Solution:
    def isValid(s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return not stack
        

"""
Notes:

    * What I learned:
        - if you put a string into a list() type conversion it will make a list of characters in that string
            eg: s = "hello" => my_list = list(s) => my_list = ['h', 'o', 'l', 'l', 'o']
            Its time complexity is O(n)

    * What I can work on:
        - Visualization of the two stacks in your solution could have been faster if you used
          a tool to visualize your thoughts
"""