'''
Link : https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2025-10-27
Time Complexity : O(n*m) where n is number of rows and m is number of columns
'''

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams, prev = 0,0

        for row in bank:
            ones = row.count('1')

            if ones > 0:
                beams += prev * ones
                prev = ones

        return beams



        
