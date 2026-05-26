'''
Link : https://leetcode.com/problems/maximum-units-on-a-truck/
'''
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True) # Remember This Syntax
        totalUnits = 0
        
        for numBoxes, numUnits in boxTypes:
            if numBoxes < truckSize:
                truckSize -= numBoxes
                totalUnits += numBoxes * numUnits
            else:
                totalUnits += truckSize * numUnits
                break
        return totalUnits 

# Alternative Solution : Time Complexity O(n) same as above
class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        i = -1
        
        for j in range(len(s)):
            if s[j] == '6':
                i = j
                break
        
        if i == -1:
            return num
        else:
            return int(s[:i] + '9' + s[i+1:])