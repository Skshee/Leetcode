'''
Link : https://leetcode.com/problems/minimum-common-value/
'''

# Set method 
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        seen = set(nums1)
        ans = []

        for num in nums2:
            if num in seen:
                ans.append(num)
        if (len(ans) == 0):
            return -1
        else:
            return min(ans)
        

# Two Pointer method
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return -1

