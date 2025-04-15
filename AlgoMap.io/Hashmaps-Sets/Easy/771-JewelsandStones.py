"""
Easy
771. Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/description/

Time to solve: 4:57
"""


"""
Problem Description:

You're given strings jewels representing the types of stones that are
jewels, and stones representing the stones you have. Each character in stones
is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.

"""


"""
My First Solution: Accepted √
In this solution I use a hash set which I do the following:
1. Create the hash-set and populate with the jewels.
2. Add all of the viable stones to the hashset.
3. Count all of the added stones, and return the values.
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        # Populate a set with jewels
        jewels_set = {}
        for x in jewels:
            jewels_set[x] = 0

        # Add stones to set
        for x in stones:
            if x in jewels_set:
                jewels_set[x] += 1
        
        # Count all stones in set and return value
        return_value = 0

        for x in jewels_set.values():
            return_value += x
        
        return return_value
    
"""
My second solution: Uses a n^2 solution. Shorter code, but longer time complexity
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        num_jewels = 0

        for x in stones:
            if x in jewels:
                num_jewels += 1
        
        return num_jewels


"""
Greg Hogg's Optimal Solution: 
 - Similar to my first answer, but the creation of the set is done much simpler.
 - I did an extra loop to add data to the hashset, however this is not necessary,
   and is faster without it.
"""

# Optimal Solution
class Solution:
    def numJewelsInStones (self, jewels: str, stones: str) -> int:
        # O(n + m)
        s = set(jewels)
        count = 0
        for stone in stones:
            if stone in s:
                count += 1
        return count

# Time Complexity: O(n + m)
# Space Complexity: O(n)

"""
Notes:

What I learned: 
    * New way to create a set with: s = set(jewels)

What I can improve on:
    * 

Key takeaways:
    * Frequency counting: Very common in string problems

    * Set usage: For fast lookups and uniqueness

    * Multiple inputs interaction: Where the relationship between two collections matters

    * Simplicity hiding insights: Easy problems sometimes train important instincts for harder ones
"""

