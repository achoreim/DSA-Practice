"""
Medium
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/description/

Time for first solution: 
Time to compile all solutions and notes: 
"""

"""
Problem Description:

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

"""
My First Solution:
"""

"""
Notes:

    * What I Learned:

    * What I can work on:
        - Initializing list of lists
"""

"""
My First Soltution: Time Limit Exceeded: Simple nested for loop
What makes this solutin slow are the repeated calls to the Counter() method.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        output.append([strs[0]])

        for x in strs[1:]:
            x_set = Counter(x)
            for i, y in enumerate(output):
                y_set = Counter(y[0])
                if x_set == y_set:
                    output[i].append(x)
                    break
            if(x_set != y_set):
                output.append([x])

        return output
    
                
"""
My Second Solution: Attempting to remove a Counter() call in the nested for loop.
Still time limit exceeded:
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        output.append([strs[0]])

        # Adding an array that keeps tracks of counter dicts to not recall them inside loop
        output_counts = []
        output_counts.append([Counter(strs[0])])

        for x in strs[1:]:
            x_set = Counter(x)
            for i, y in enumerate(output):
                y_set = output_counts[i][0]
                if x_set == y_set:
                    output[i].append(x)
                    break
            if(x_set != y_set):
                output.append([x])
                output_counts.append([x_set])

        return output

