"""
Easy
1189. Maximum Number of Balloons
https://leetcode.com/problems/maximum-number-of-balloons/description/

Time for first solution: 10:00 (Didnt Work) 15:17 (For First working solution)
Time to compile all solutions and notes: 43:27
"""

"""
Problem Description:

Given a string text, you want to use the characters of text
to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the
maximum number of instances that can be formed.

 

Example 1:

Input: text = "nlaebolko"
Output: 1
Example 2:


Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
 

Note: This question is the same as 2287: Rearrange Characters to Make Target String.
"""

"""
My First Solution: Using the set() class

Solution not accpeted: Fails the text case of "balon"

Time this solution took: 10:00
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count = 0

        b_set = set("balloon")

        text_set = set()

        empty_set = set()

        for x in text:
            if x in b_set:
                text_set.add(x)
            if text_set == b_set:
                count += 1
                text_set.clear()

        return count


"""
My Second Solution: Using the Counter() class
Time Taken for this soltion: 15:17
This solution involvs three different steps, and each was created after
running into a different edge case after running code.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count the text
        text_dict = Counter(text)

        # Remove all of the non 'balloon' key value pairs
        for x in list(text_dict):
            if x not in "balloon":
                text_dict.pop(x)

        # If length is less than 5 return 0
        if len(text_dict) < 5:
            return 0
        

        # Find minimum value from count
        min = float(inf)

        for x in text_dict:
            val = text_dict[x]
            # Divide 'l' and 'o' by 2 because they apear twice in 'balloon'
            if (x == "l") or (x == "o"):
                val = val//2

                if val == 0:
                    return 0
            if val < min:
                min = val
        
        # Return min value
        return min
    
"""
Greg Hogg's Optimal Solution:
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon = "balloon"
        
        for c in text:
            if c in balloon:
                counter[c] += 1
        
        if any(c not in counter for c in balloon):
            return 0
        else:
            return min(counter["b"], counter["a"], counter["l"] // 2, counter["o"] // 2, counter["n"])

# Time Complexity: O(n)
# Space Complexity: O(1)


"""
Notes:

    * What I Learned: 
        - 'set("balloon")' will make a set of characters
        - You can reset a set with 'set.clear()'
        - You can add a value to a set with 'set.add()'
        - You can not remove a character from a string in O(1) time because python strings are immutable
        - You can do lower bound division with //: 'val = val//2'
        - Remove a key value pair from a dictionary:
            - If you are iterating throught the dict, make sure you use a copy of the dict in the iterator
              otherwise python will throw an error: 
                - Use the following loop header (This creats a copy of the dict keys): for x in list(my_dict): 
        - Remove a key value pair froma dict with '.pop(key)'

    * What I Can Work On:
        - I made the same mistake with other problems, using the set() class when the solution required
          the counter() clsss
        - Implement Default Dicts, when applicable.
"""


