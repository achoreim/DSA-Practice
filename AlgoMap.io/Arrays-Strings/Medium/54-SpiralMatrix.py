"""
Medium
54. Spiral Matrix
https://leetcode.com/problems/spiral-matrix/description/

Time to solve:
"""

"""
Problem Description:

Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

"""
My First Solution:

A clever solution using multipl try-except statements inside a while loop. 
This solution was not accepted as it exceeded the time limit.
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Order of Spiral:
        # First: Right
        # Second: Down
        # Third: Left
        # Fourth: Up

        output = []

        previousPositions = []


        output.append(matrix[0][0])
        coords = [0,0]
        previousPositions.append(coords)

        while True:

            #Go Right:
            try:
                right = [coords[0], coords[1]+1]
                value = matrix[right[0]][right[1]]
                if right not in previousPositions:
                    previousPositions.append(right)
                    output.append(value)
                    coords = right
            except:
                #Go Down:
                try:
                    down = [coords[0]+1, coords[1]]
                    value = matrix[down[0]][down[1]]
                    if down not in previousPositions:
                        previousPositions.append(down)
                        output.append(value)
                        coords = down
                
                except:
                    #Go Left:
                    try:
                        left = [coords[0], coords[1]-1]
                        value = matrix[left[0]][left[1]]
                        if left not in previousPositions:
                            previousPositions.append(left)
                            output.append(value)
                            coords = left
                    except:
                        #Go Up:
                        try:
                            up = [coords[0]-1, coords[1]]
                            value = matrix[up[0]][up[1]]
                            if left not in previousPositions:
                                previousPositions.append(up)
                                output.append(value)
                                coords = up
                        except:
                            break
        return output


"""

"""