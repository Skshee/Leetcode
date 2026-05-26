'''
Link : https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/?envType=daily-question&envId=2025-06-10

Question of the day : 10/6/25
'''

class Solution:
    def maxDifference(self, s: str) -> int:
        evenList = []
        oddList = []
        diff = []
        Counts = Counter(s)
        
        for i in Counts:
            if(Counts[i] % 2 == 0):
                evenList.append(Counts[i])
            else:
                oddList.append(Counts[i])

        return max(oddList) - min(evenList)
        