"""
Easy
1768. Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/description/
"""


"""
Problem Description:

You are given two strings word1 and word2. Merge the strings by adding
letters in alternating order, starting with word1. If a string is longer
than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""


"""
My 1st Solution:

Time complexity: O(n^2) -> This is because using the '+=' operation results in linear time O(n) by itself 
"""



class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Error Check for empty strings:
        if not word1 and not word2:
            return ""
        
        # Initialize output variable
        outputStr = ""

        # Set upper iteration limit to smaller word
        limit = word1
        usingWord1 = True
        if len(word1) > len(word2):
            limit = word2
            usingWord1 = False

        # Iterate over smaller word and add characters alternately
        for x in range(0, len(limit)):
            outputStr += word1[x]
            outputStr += word2[x]

        # Append the rest of the longer word to the outputStr
        if usingWord1:
            outputStr += word2[x+1:]
        else:
            outputStr += word1[x+1:]

        # Return output Str
        return outputStr
    


"""
My updated Solution:

Changes: (Resulted in a faster time complexity)
    -> Instead of using '+=' I made the outputStr into a List and then used ''.join()
        -> This is becasue the '+=' function is linear: O(n) while the .append() is constant O(1)
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Error Check for empty strings:
        if not word1 and not word2:
            return ""
        
        # Initialize output List
        outputList = []

        # Set upper iteration limit to smaller word
        limit = word1
        usingWord1 = True
        if len(word1) > len(word2):
            limit = word2
            usingWord1 = False

        # Iterate over smaller word and add characters alternately to list
        # This is an O(n) operation on its own as the .append() is O(1)
        for x in range(0, len(limit)):
            outputList.append(word1[x])
            outputList.append(word2[x]) 

        # Append the rest of the longer word to the outputList
        if usingWord1:
            outputList.append(word2[x+1:])
        else:
            outputList.append(word1[x+1:])

        # Return the joined list, this is O(n) operation on its own
        return ''.join(outputList)

"""

Solution Description:
    1. First I find which word is shorter than the other and use that for the main interation loop
    2. I then iterate over the shorter word and append each letter from both words one at a time
    3. Next I append the rest of the large word (If there is one) and return that as the asnwer
    (Joining lists as needed)

Notes:

    What I learned: 
        Strings in Python are immutable — every += creates a new string, copying all previous
        content. Repeated += in a loop causes the program to copy the growing string over and over,
        resulting in O(n²) time. Using a list with .append() is O(1) per operation. At the end, ''.join(list)
        combines everything in O(n) time. This makes .append() + join() much faster and more
        memory-efficient for building strings.



    Mistakes I Made: 
        -> I used .append() instead of '+' for appending a string to a string: (DNE in Python)
            -> outputStr.append(word1[x]) instead of outputStr += word[x]
            -> using += on a string results in an O(n) operation, better to append to a list then join
"""