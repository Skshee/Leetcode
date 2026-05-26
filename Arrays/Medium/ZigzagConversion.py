'''
Link: https://leetcode.com/problems/zigzag-conversion/
Time Complexity : O(n)
LeetCode Problem: 6. Zigzag Conversion
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        currRow = 0
        direction = 1
        i = 0
        Row = [""] * (numRows)

        if numRows == 1:
            return s
        
        while i < len(s):
            Row[currRow] += s[i] # Appending in Strings
            # Base condition where direction changes
            if currRow == 0:
                direction = 1
            elif currRow == numRows - 1:
                direction = -1

            currRow = currRow + direction
            i += 1
        
        return ''.join(Row)
